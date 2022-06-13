import requests
import os
import logging
import dbutils
import messages
import random
import string
import datetime
from telebot import TeleBot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dbutils import States, Roles
from messages import get_response
from io import BytesIO

logging.basicConfig(level=logging.DEBUG)

BACKEND_URL = "http://backend"

FINISH_PHRASES = ["сохранить", "закончить", "конец", "finish"]

bot = TeleBot(os.getenv("telegram_token"), parse_mode=None)


def check_state(client_id: int, state: States) -> bool:
    return dbutils.get_state(client_id) == state


def get_client_id(message: Message) -> int:
    return message.chat.id


def get_user_id(message: Message) -> int:
    return dbutils.get_user_by_telegram_id(message.from_user.id)


def do_transition(bot: TeleBot, message: Message, state: States):
    logging.debug(f"Transitting to state {state}")
    dbutils.set_state(get_client_id(message), state)
    response = get_response(state.value)
    bot.send_message(
        message.chat.id, text=response["message"], reply_markup=response["keyboard"]
    )


@bot.message_handler(commands=["start"])
def user_login(message):
    '''Состояние "пользователь только что запустил бота"'''
    logging.debug("State: User Login")
    user_id = get_user_id(message)
    if user_id:
        logging.debug(f"User exists: id={user_id}")
        do_transition(bot, message, States.MENU)
    else:
        do_transition(bot, message, States.REGISTRATION)


@bot.message_handler(commands=["godmode"])
def godmode(message):
    """Вызвавший функцию пользователь станет администратором"""
    logging.debug(f"Adding admin user with telegram id {message.from_user.id}")
    user_id = get_user_id(message)
    if user_id:
        logging.debug(f"User exists: id={user_id}. Setting admin role")
        dbutils.set_user_role(user_id, Roles.ADMIN)
    else:
        user_id = dbutils.create_user("admin", Roles.ADMIN, generate_token())
        dbutils.add_telegram_id_to_user(user_id, message.from_user.id)
        logging.debug(f"Admin created with id={user_id}")
    do_transition(bot, message, States.MENU)


@bot.message_handler(
    func=lambda message: check_state(get_client_id(message), States.REGISTRATION)
)
def register_user(message):
    '''Состояние "регистрация пользователя по коду приглашения"'''
    token = message.text
    logging.debug(f"Got token {token}")
    user_id = dbutils.get_user_by_token(token)
    if not user_id:
        bot.send_message(
            message.chat.id, "Неверный токен! Проверьте правильность и введите заново"
        )
        return
    else:
        logging.debug(f"Found user with id: {user_id}")
        dbutils.add_telegram_id_to_user(user_id, message.from_user.id)
        do_transition(bot, message, States.MENU)


@bot.message_handler(
    func=lambda message: check_state(get_client_id(message), States.MENU)
)
def menu(message):
    logging.debug("State: main menu")
    choice = message.text
    if choice == "Добавить новость":
        do_transition(bot, message, States.NEWS_ADD)
    elif choice == "Добавить документ":
        do_transition(bot, message, States.DOCUMENT_ADD)
    elif message.text == "Добавить питание":
        do_transition(bot, message, States.MEALS_ADD)
    elif message.text == "Показать новости":
        show_news(message)
    elif message.text == "Показать документы":
        show_docs(message)
    elif message.text == "Добавить пользователя":
        user_id = get_user_id(message)
        if dbutils.get_user_role(user_id) == Roles.ADMIN:
            do_transition(bot, message, States.USER_ADD)
        else:
            bot.send_message(
                message.chat.id, "Извините, но у вас нет прав на это действие"
            )
    else:
        bot.send_message(
            message.chat.id,
            text="Пожалуйста, выберите действие из предложенных",
            reply_markup=messages.main_menu_keyboard,
        )


def show_news(message):
    logging.debug("Get and show news list")
    response = requests.get(f"{BACKEND_URL}/news/")
    if response.status_code == 200:
        news_list = response.json()
        for news in news_list:
            markup = InlineKeyboardMarkup()
            edit_button = InlineKeyboardButton(text="Редактировать", callback_data=f"edit news {news._id}")
            delete_button = InlineKeyboardButton(text="Удалить", callback_data = f"delete news {news._id}")
            markup.add(edit_button, delete_button)
            bot.send_message(
                message.chat.id,
                text=f'{news.title}',
                reply_markup=markup
                )

def show_docs(message):
    logging.debug("Get and show docs list")
    response = requests.get(f"{BACKEND_URL}/docs/")
    if response.status_code == 200:
        doc_list = response.json()
        for doc in doc_list:
            markup = InlineKeyboardMarkup()
            edit_button = InlineKeyboardButton(text="Редактировать", callback_data=f"edit doc {doc._id}")
            delete_button = InlineKeyboardButton(text="Удалить", callback_data = f"delete doc {doc._id}")
            markup.add(edit_button, delete_button)
            bot.send_message(
                message.chat.id,
                text=f'{doc.title}',
                reply_markup=markup
                )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        logging.debug(f"Callback handler: {call.data}")
        action, entity, id = call.data.split(' ')
        logging.debug(f"Do action {action} with {entity} id {id}")
        if action == "delete":
            requests.delete(f"{BACKEND_URL}/{entity}/{id}")
        elif action == "edit":
            client_id = get_client_id(call.message)
            dbutils.update_context(client_id, {"edited_id": id})
            if entity == "doc":
                do_transition(bot, message, States.DOCUMENT_BODY)
            elif entity == "news":
                do_transition(bot, message, States.NEWS_BODY)

@bot.message_handler(
    func=lambda message: check_state(get_client_id(message), States.USER_ADD)
)
def user_add(message):
    logging.debug("State: user add")
    role = message.text
    dbutils.update_context(get_client_id(message), {"user_role": role})
    do_transition(bot, message, States.USER_NAME)


@bot.message_handler(
    func=lambda message: check_state(get_client_id(message), States.USER_NAME)
)
def user_name(message):
    logging.debug("State: user name")
    name = message.text
    token = generate_token()
    role = dbutils.get_context(get_client_id(message))["user_role"]
    dbutils.create_user(name, Roles(role), token)
    dbutils.update_context(get_client_id(message), {"user_role": ""})
    bot.send_message(
        message.chat.id,
        text=f"Создан пользователь с ролью {role} и кодом регистрации {token}",
    )
    do_transition(bot, message, States.MENU)


@bot.message_handler(
    func=lambda message: check_state(get_client_id(message), States.NEWS_ADD)
)
def news_add(message):
    logging.debug("State: news add")
    title = message.text
    dbutils.update_context(get_client_id(message), {"news_title": title})
    do_transition(bot, message, States.NEWS_CATEGORY)


@bot.message_handler(
    func=lambda message: check_state(get_client_id(message), States.NEWS_CATEGORY)
)
def news_category(message):
    logging.debug("State: news category")
    title = message.text
    dbutils.update_context(get_client_id(message), {"news_category": title})
    do_transition(bot, message, States.NEWS_BODY)


@bot.message_handler(
    func=lambda message: check_state(get_client_id(message), States.NEWS_BODY),
    content_types=["text", "photo"],
)
def news_body(message):
    logging.debug("State: news body")
    client_id = get_client_id(message)
    context = dbutils.get_context(client_id)
    if message.text:
        logging.debug(f"Message contains text: {message.text}")
        text = message.text

        # Если пользователь закончил редактирование сообщения и хочет его сохранить,
        # сохранем и возвращаем его в главное меню.
        if text.lower() in FINISH_PHRASES:
            logging.debug(
                f"We have a message with text {context.get('news_text')} and photos {context.get('news_photo')}"
            )
            title = context.get("news_title", "Нет заголовка")
            text = context.get("news_text", "")
            category = context.get("news_category", "")
            photo_array = context.get("news_photo", [])
            for photo in photo_array:
                bot.get_file_url(photo)
            # TODO: аплоад фотографий
            edited_id = context.get("edited_id")
            if edited_id:
                response = requests.put(
                    f"{BACKEND_URL}/news/{edited_id}",
                    json={
                        "title": title,
                        "category": category,
                        "text": text,
                    },
                )
            else:
                response = requests.post(
                    f"{BACKEND_URL}/news/",
                    json={
                        "title": title,
                        "category": category,
                        "text": text,
                    },
                )
            if response.status_code == 200:
                bot.send_message(message.chat.id, "Успешно отправлено!")
                # Очистка контекста - чтобы в следующий раз новость начиналась с нуля
                dbutils.update_context(
                    client_id,
                    {
                        "news_title": "",
                        "news_category": "",
                        "news_text": "",
                        "news_photo": [],
                    },
                )
            else:
                bot.send_message(message.chat.id, "Не отправлено...")
            do_transition(bot, message, States.MENU)
            return

        old_text = context.get("news_text", "")
        dbutils.update_context(client_id, {"news_text": old_text + text})

    elif message.photo:
        logging.debug(f"Message contains photos: {len(message.photo)} files")
        photo = [photo.file_id for photo in message.photo]
        old_photo = context.get("news_photo", [])
        dbutils.update_context(client_id, {"news_photo": old_photo + photo})


@bot.message_handler(
    func=lambda message: check_state(get_client_id(message), States.DOCUMENT_ADD)
)
def document_add(message):
    logging.debug("State: document add")
    title = message.text
    dbutils.update_context(get_client_id(message), {"document_title": title})
    do_transition(bot, message, States.DOCUMENT_BODY)


@bot.message_handler(
    func=lambda message: check_state(get_client_id(message), States.DOCUMENT_BODY),
    content_types=["document"],
)
def document_body(message):
    logging.debug("State: document body")
    client_id = get_client_id(message)
    context = dbutils.get_context(client_id)
    title = context.get("document_title", "Нет заголовка")
    file_id = message.document.file_id
    file_name = message.document.file_name
    extension = file_name.split(".")[-1]
    url = bot.get_file_url(file_id)
    # TODO: аплоад документа
    edited_id = context.get("edited_id")
    if edited_id:
        response = requests.put(
            f"{BACKEND_URL}/docs/{edited_id}",
            json={
                "title": title,
                "type": extension,
                "url": url,
                "date": str(datetime.datetime.now()),
                "author": dbutils.get_user_name(get_user_id(message)),
            },
        )
    else:
        response = requests.post(
            f"{BACKEND_URL}/docs/",
            json={
                "title": title,
                "type": extension,
                "url": url,
                "date": str(datetime.datetime.now()),
                "author": dbutils.get_user_name(get_user_id(message)),
            },
        )
    if response.status_code == 200:
        bot.send_message(message.chat.id, "Успешно отправлено!")
        dbutils.update_context(client_id, {"document_title": ""})
    else:
        bot.send_message(message.chat.id, "Не отправлено...")
    do_transition(bot, message, States.MENU)


@bot.message_handler(
    func=lambda message: check_state(get_client_id(message), States.MEALS_ADD),
    content_types=["text", "document"],
)
def meals_add(message):
    logging.debug("State: meals add")
    client_id = get_client_id(message)
    if message.text and message.text == "Загрузить шаблон":
        with open("templates/template_menu.xlsx", "rb") as template_menu:
            file_object = BytesIO(template_menu.read())
            file_object.name = "Шаблон меню питания.xlsx"
            bot.send_document(
                message.from_user.id, data=file_object, caption="Шаблон меню питания"
            )
    elif message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name
        extension = file_name.split(".")[-1]
        url = bot.get_file_url(file_id)
        # TODO: загрузить таблицу и обработать
        response = requests.post(
            f"{BACKEND_URL}/meals/",
            json={
                "date": str(datetime.datetime.now()),
                "breakfast": {
                    "hot_meal": "string",
                    "hot_drink": "string",
                    "fruit": "string",
                    "milk": "string",
                    "bakery": "string",
                },
                "second_breakfast": {"hot_drink": "string", "snack": "string"},
                "dinner": {
                    "hot_meal_first": "string",
                    "hot_meal_second": "string",
                    "garnish": "string",
                    "drink": "string",
                    "bread_white": "string",
                    "bread_black": "string",
                    "snack": "string",
                },
            },
        )
        if response.status_code == 200:
            bot.send_message(message.chat.id, "Успешно отправлено!")
        else:
            bot.send_message(message.chat.id, "Не отправлено...")
    do_transition(bot, message, States.MENU)


def generate_token():
    letters = string.ascii_lowercase
    rand_string = "".join(random.choice(letters) for i in range(8))
    return rand_string


bot.infinity_polling()
