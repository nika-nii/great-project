from telebot import types

TRANSITIONS = {
    "main_menu": {
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
    "users": {
        "message": "Какие права будут выданы пользователю?",
        "keyboard": [
            "Администратор",
            "Редактор"
        ]
    },
    "news_title": {
        "message": "Введите заголовок статьи",
        "keyboard": []
    },
    "news_body": {
        "message": "Введите текст статьи",
        "keyboard": []
    },
    "documents_title": {
        "message": "Введите заголовок статьи",
        "keyboard": []
    },
    "documents_body": {
        "message": "Введите текст статьи",
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
