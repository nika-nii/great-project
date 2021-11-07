import telebot

bot = telebot.TeleBot("2066709794:AAELn19fE-WExz8LOh9xrz9yeWf5xzR3bKk", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я школьный бот!")

@bot.message_handler(func=lambda m: m.text == "test")
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()