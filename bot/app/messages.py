from telebot import types

TRANSITIONS = {
    "menu": {
        "message": "Главное меню",
        "keyboard": [
            "Добавить новость",
            "Добавить документ",
            "Добавить пользователя"
        ]
    },
    "registration": {
        "message": "Вам необходимо зарегистрироваться. Введите код приглашения",
        "keyboard": []
    },
    "user_add": {
        "message": "Какие права будут выданы пользователю?",
        "keyboard": [
            "Администратор",
            "Редактор"
        ]
    },
    "user_name": {
        "message": "Укажите имя пользователя",
        "keyboard": []
    },
    "news_add": {
        "message": "Введите заголовок статьи",
        "keyboard": []
    },
    "news_body": {
        "message": "Добавляйте текст и изображения в одном или нескольких сообщениях. Для окончания редактирования введите слово 'конец'",
        "keyboard": []
    },
    "news_body": {
        "message": "Введите текст статьи",
        "keyboard": []
    },
    "documents_add": {
        "message": "Введите заголовок статьи",
        "keyboard": []
    },
    "documents_body": {
        "message": "Введите текст статьи",
        "keyboard": []
    },
    "meals_add": {
        "message": "Введите название меню",
        "keyboard": []
    }
}

def get_response(transition):
    value = TRANSITIONS.get(transition)
    if not value:
        raise ValueError("Переход в данное состояние не описан")
    message = value["message"]
    keyboard = None
    if value["keyboard"]:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for k in value["keyboard"]:
            keyboard.add(types.KeyboardButton(k))
    else:
        keyboard = types.ReplyKeyboardRemove()
    return {
        "message": message,
        "keyboard": keyboard
    }
