from telebot import types

# Переход в состояние Главное меню
main_menu_message = "Главное меню"
main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_keyboard.add(
    types.KeyboardButton("Добавить новость"),
    types.KeyboardButton("Добавить документ"),
    types.KeyboardButton("Добавить пользователя")
)

# Переход в состояние регистрация
registration_message = "Вам необходимо зарегистрироваться. Введите код приглашения"
registration_keyboard = types.ReplyKeyboardRemove()

# Переход в состояние Добавление пользователя
users_message = "Какие права будут выданы пользователю?"
users_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
users_keyboard.add(
    types.KeyboardButton("admin"),
    types.KeyboardButton("editor")
)

# Переход в состояние Добавление новости
news_title_message = "Введите заголовок статьи"
news_title_keyboard = types.ReplyKeyboardRemove()

news_category_message = "Введите категорию"
news_category_keyboard = types.ReplyKeyboardRemove()

news_text_message = "Введите текст статьи"
news_text_keyboard = types.ReplyKeyboardRemove()

# Переход в состояние Добавление документа
documents_title_message = "Введите заголовок статьи"
documents_title_keyboard = types.ReplyKeyboardRemove()

documents_file_message = "Введите категорию"
documents_file_keyboard = types.ReplyKeyboardRemove()

# Переход в состояние Редактирование пользователя
users_message = "Какие права будут выданы пользователю?"
users_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
users_keyboard.add(
    types.KeyboardButton("admin"),
    types.KeyboardButton("editor")
)
