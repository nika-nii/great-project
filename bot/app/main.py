import telebot
import requests
import os
import logging
import dbutils
import messages
import random
import string
import datetime
from telebot.types import Message, TeleBot
from dbutils import States,Roles
from messages import get_response

logging.basicConfig(level=logging.DEBUG)

BACKEND_URL = "http://backend"

bot = telebot.TeleBot(os.getenv('telegram_token'), parse_mode=None)

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
        message.chat.id,
        text=response.message,
        reply_markup=response.keyboard
    )

@bot.message_handler(commands=['start'])
def user_login(message):
    '''Состояние "пользователь только что запустил бота"'''
    logging.debug('State: User Login')
    user_id = get_user_id(message)
    if user_id:
        logging.debug(f'User exists: id={user_id}')
        do_transition(bot, message, States.MENU)
    else:
        do_transition(bot, message, States.REGISTRATION)

@bot.message_handler(commands=['godmode'])
def godmode(message):
    '''Вызвавший функцию пользователь станет администратором'''
    logging.debug(f'Adding admin user with telegram id {message.from_user.id}')
    user_id = get_user_id(message)
    if user_id:
        logging.debug(f'User exists: id={user_id}. Setting admin role')
        dbutils.set_user_role(user_id, Roles.ADMIN)
    else:
        user_id = dbutils.create_user("admin", Roles.ADMIN, generate_token())
        dbutils.add_telegram_id_to_user(user_id, message.from_user.id)
        logging.debug(f'Admin created with id={user_id}')
    do_transition(bot, message, States.MENU)

@bot.message_handler(func=check_state(get_client_id(message), States.REGISTRATION))
def register_user(message):
    '''Состояние "регистрация пользователя по коду приглашения"'''
    token = message.text
    logging.debug(f'Got token {token}')
    user_id = dbutils.get_user_by_token(token)
    if not user_id:
        bot.send_message(
            message.chat.id,
            "Неверный токен! Проверьте правильность и введите заново"
        )
        return
    else:
        logging.debug(f'Found user with id: {user_id}')
        dbutils.add_telegram_id_to_user(user_id, message.from_user.id)
        do_transition(bot, message, States.MENU)

@bot.message_handler(func=check_state(get_client_id(message), States.MENU))
def menu(message):
    logging.debug("State: main menu")
    choice = message.text
    if choice == "Добавить новость":
        do_transition(bot, message, States.NEWS_ADD)
    elif choice == "Добавить документ":
        do_transition(bot, message, States.DOCUMENT_ADD)
    elif message.text == "Добавить питание":
        do_transition(bot, message, States.MEALS_ADD)
    elif message.text == "Добавить пользователя":
        user = get_user_id(message)
        if user["role"] == Roles.ADMIN.value:
            do_transition(bot, message, States.USER_ADD)
        else:
            bot.send_message(message.chat.id, "Извините, но у вас нет прав на это действие")
    else:
        bot.send_message(
            message.chat.id, 
            text = 'Пожалуйста, выберите категорию из предложенных',
            reply_markup = messages.main_menu_keyboard
        )

@bot.message_handler(func=check_state(get_client_id(message), States.USER_ADD))
def user_add(message):
    logging.debug("State: user add")
    role = message.text
    dbutils.update_context(get_client_id(message), {"user_role": role})
    do_transition(bot, message, States.USER_NAME)
    
@bot.message_handler(func=check_state(get_client_id(message), States.USER_NAME))
def user_name(message):
    logging.debug("State: user name")
    name = message.text
    token = generate_random_string(8)
    role = dbutils.get_context(get_client_id(message))["user_role"]
    dbutils.create_user(name, role, token)
    dbutils.update_context(get_client_id(message), {"user_role": ""})
    bot.send_message(
        message.chat.id,
        text = f"Создан пользователь с ролью {role} и кодом регистрации {token}"
    )
    do_transition(bot, message, States.MENU)

@bot.message_handler(func=check_state(get_client_id(message), States.NEWS_ADD))
def news_add(message):
    logging.debug("State: news add")
    title = message.text
    dbutils.update_context(get_client_id(message), {"news_title": title})
    do_transition(bot, message, States.NEWS_BODY)
    
@bot.message_handler(func=check_state(get_client_id(message), States.NEWS_BODY))
def news_body(message):
    logging.debug("State: news body")
    # TODO: получить от пользователя прикрепленную картинку, сохранить ее к себе
    if message.text:
        logging.debug(f"Message contains text: {message.text}")
        text = message.text
        old_text = dbutils.get_context(get_client_id(message))["news_text"]
        dbutils.update_context(client_id, {"news_text": old_text + text})
    elif message.photo:
        logging.debug(f"Message contains photos: {len(message.photo)} files")
        photo = [photo.file_id for photo in message.photo]
        # TODO: key get from dict
        old_photo = dbutils.get_context(get_client_id(message))["news_photo"]
        dbutils.update_context(client_id, {"news_photo": old_photo + photo})
    text = message.text
    token = generate_random_string(8)
    role = dbutils.get_context(get_client_id(message))["user_role"]
    dbutils.create_user(name, role, token)
    bot.send_message(
        message.chat.id,
        text = f"Создан пользователь с ролью {role} и кодом регистрации {token}"
    )
    do_transition(bot, message, States.MENU)

@bot.message_handler(func=lambda message: dbutils.get_state(message.chat.id) == "news-title")
def users(message):
    logging.debug(f'We are in news title menu')

    title = message.text
    dbutils.news_add_title(dbutils.get_state_document(message.chat.id), title)

    dbutils.set_state(message.chat.id, "news-category")
    bot.send_message(
        message.chat.id, 
        text = messages.news_category_message,
        reply_markup = messages.news_category_keyboard
        )

@bot.message_handler(func=lambda message: dbutils.get_state(message.chat.id) == "news-category")
def users(message):
    logging.debug(f'We are in news category menu')

    category = message.text
    dbutils.news_add_category(dbutils.get_state_document(message.chat.id), category)

    dbutils.set_state(message.chat.id, "news-text")
    bot.send_message(
        message.chat.id, 
        text = messages.news_text_message,
        reply_markup = messages.news_text_keyboard
        )

@bot.message_handler(func=lambda message: dbutils.get_state(message.chat.id) == "news-text")
def users(message):
    logging.debug(f'We are in news text menu')

    text = message.text
    dbutils.news_add_text(dbutils.get_state_document(message.chat.id), text)

    news = dbutils.news_get(dbutils.get_state_document(message.chat.id))

    response = requests.post(
        f'{BACKEND_URL}/news/', 
        json={
            'title': news["title"], 
            'category': news["category"], 
            'text': news["text"]
            }
        )
    if response.status_code == 200:
        bot.send_message(message.chat.id, "Успешно отправлено!")
    else:
        bot.send_message(message.chat.id, "Не отправлено...")

    dbutils.set_state(message.chat.id, "main-menu")
    bot.send_message(
        message.chat.id, 
        text = messages.main_menu_message,
        reply_markup = messages.main_menu_keyboard
        )

@bot.message_handler(func=lambda message: dbutils.get_state(message.chat.id) == "documents-title")
def users(message):
    logging.debug(f'We are in documents title menu')

    title = message.text
    dbutils.document_add_title(dbutils.get_state_document(message.chat.id), title)

    dbutils.set_state(message.chat.id, "documents-file")
    bot.send_message(
        message.chat.id, 
        text = messages.documents_file_message,
        reply_markup = messages.documents_file_keyboard
        )

@bot.message_handler(func=lambda message: dbutils.get_state(message.chat.id) == "documents-file", content_types=["document"])
def users(message):
    logging.debug(f'We are in documents file menu')

    file_id = message.document.file_id
    file_name = message.document.file_name
    extension = file_name.split('.')[-1]
    url = bot.get_file_url(file_id)
    dbutils.document_add_file(dbutils.get_state_document(message.chat.id), url)

    document = dbutils.document_get(dbutils.get_state_document(message.chat.id))

    response = requests.post(
        f'{BACKEND_URL}/docs/', 
        json={
            'title': document["title"], 
            'type': extension,
            'url': document["url"],
            'date': str(datetime.datetime.now()),
            'author': str(message.chat.id)
            }
        )
    if response.status_code == 200:
        bot.send_message(message.chat.id, "Успешно отправлено!")
    else:
        bot.send_message(message.chat.id, "Не отправлено...")

    dbutils.set_state(message.chat.id, "main-menu")
    bot.send_message(
        message.chat.id, 
        text = messages.main_menu_message,
        reply_markup = messages.main_menu_keyboard
        )

def generate_token():
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(8))
    return rand_string

bot.infinity_polling()
