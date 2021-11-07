import telebot
import requests

bot = telebot.TeleBot("2066709794:AAELn19fE-WExz8LOh9xrz9yeWf5xzR3bKk", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я школьный бот!")

@bot.message_handler(func=lambda m: m.text == "test")
def echo_all(message):
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['show'])
def get_news_titles(message):
    response = requests.get('http://127.0.0.1:8000/news/').json()
    reply = ''
    for news_item in response:
        reply += f'id: {news_item["id"]}, title: {news_item["title"]}\n'
    bot.reply_to(message, reply)

@bot.message_handler(func=lambda m: True)
def post_news_title(message):
    response = requests.post('http://127.0.0.1:8000/news/', json={'title': message.text, 'category': '', 'text': ''})
    if response.status_code == 200:
        bot.reply_to(message, message.text)

bot.infinity_polling()