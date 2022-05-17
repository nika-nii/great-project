import telebot
import requests
import os
import logging
import dbutils
import messages
import random
import string

logging.basicConfig(level=logging.DEBUG)

BACKEND_URL = "http://backend"

bot = telebot.TeleBot(os.getenv('telegram_token'), parse_mode=None)

@bot.message_handler(commands=['start'])
def user_login(message):
    logging.debug('Started user login')
    user = dbutils.get_system_user(message.from_user.id)
    if user:
        logging.debug(f'Found user: id={user["_id"]}')
        logging.debug("Changing state to Main menu")
        dbutils.set_state(message.chat.id, "main-menu")
        
        bot.send_message(
            message.chat.id, 
            text = messages.main_menu_message,
            reply_markup = messages.main_menu_keyboard
            )

    else:
        logging.debug(f'Changing state to Registration')
        dbutils.set_state(message.chat.id, "registration")
        bot.send_message(
            message.chat.id,
            text = messages.registration_message,
            reply_markup = messages.registration_keyboard
            )

@bot.message_handler(func=lambda message: dbutils.get_state(message.chat.id) == "registration")
def register_user(message):
    token = message.text
    logging.debug(f'Got token {token}')
    user = dbutils.get_user_by_token(token)
    logging.debug(f'Found user: {user}')
    if user:
        dbutils.link_user_to_tg(user["_id"], message.from_user.id)
        dbutils.set_state(message.chat.id, "main-menu")
    else:
        if message.text == "admin":
            dbutils.create_admin(message.from_user.id)
        bot.send_message(message.chat.id, "Пользователя с таким кодом приглашения не существует")

@bot.message_handler(func=lambda message: dbutils.get_state(message.chat.id) == "main-menu")
def main_menu(message):
    logging.debug(f'We are in main menu')
    if message.text == "Добавить новость":
        logging.debug("Changing state to News-title")
        dbutils.set_state(message.chat.id, "news-title")
        logging.debug("Creating news document")
        news_id = dbutils.news_create()
        logging.debug(f"Adding to state document id: {news_id}")
        dbutils.set_state_document(message.chat.id, news_id)
        bot.send_message(
            message.chat.id,
            text = messages.news_title_message,
            reply_markup = messages.news_title_keyboard
            )
    elif message.text == "Добавить документ":
        logging.debug("Changing state to Documents")
        dbutils.set_state(message.chat.id, "documents")
        bot.send_message(
            message.chat.id,
            text = messages.documents_message,
            reply_markup = messages.documents_keyboard
            )
    elif message.text == "Добавить питание":
        logging.debug("Changing state to Meals")
        dbutils.set_state(message.chat.id, "meals")
        bot.send_message(
            message.chat.id,
            text = messages.meals_message,
            reply_markup = messages.meals_keyboard
            )
    elif message.text == "Добавить пользователя":
        logging.debug("Changing state to Users")
        dbutils.set_state(message.chat.id, "users")
        bot.send_message(
            message.chat.id,
            text = messages.users_message,
            reply_markup = messages.users_keyboard
            )
    else:
        bot.send_message(
            message.chat.id, 
            text = messages.main_menu_message,
            reply_markup = messages.main_menu_keyboard
            )

@bot.message_handler(func=lambda message: dbutils.get_state(message.chat.id) == "users")
def users(message):
    logging.debug(f'We are in users menu')
    user = dbutils.get_system_user(message.from_user.id)
    if user["role"] != "admin":
        bot.send_message(message.chat.id, "Извините, но у вас нет прав на это действие")
    else:
        role = message.text
        token = generate_random_string(8)
        dbutils.create_user(role, token)
        bot.send_message(
            message.chat.id,
            text = f"Создан пользователь с ролью {role} и кодом регистрации {token}"
            )
    dbutils.set_state(message.chat.id, "main-menu")
    bot.send_message(
        message.chat.id, 
        text = messages.main_menu_message,
        reply_markup = messages.main_menu_keyboard
        )

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

# @bot.message_handler(commands=['show'])
# def get_news_titles(message):
#     response = requests.get(f'{BACKEND_URL}/news/').json()
#     reply = 'Вот что я тебе скажу. \n'
#     for news_item in response:
#         reply += f'id: {news_item["_id"]}, title: {news_item["title"]}\n'
#     bot.reply_to(message, reply)

# @bot.message_handler(func=lambda m: True)
# def post_news_title(message):
#     response = requests.post(f'{BACKEND_URL}/news/', json={'title': message.text, 'category': '', 'text': ''})
#     if response.status_code == 200:
#         bot.reply_to(message, message.text)

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


bot.infinity_polling()