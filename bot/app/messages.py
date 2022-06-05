from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

TRANSITIONS = {
    "menu": {
        "message": "Главное меню",
        "keyboard": [
            "Добавить новость",
            "Добавить документ",
            "Добавить питание",
            "Добавить пользователя",
            "Показать новости",
            "Показать документы"
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
    "news_category": {
        "message": "Укажите категорию статьи",
        "keyboard": []
    },
    "news_body": {
        "message": "Добавляйте текст и изображения в одном или нескольких сообщениях. Для окончания редактирования введите слово 'конец'",
        "keyboard": []
    },
    "document_add": {
        "message": "Введите название документа",
        "keyboard": []
    },
    "document_body": {
        "message": "Прикрепите файл",
        "keyboard": []
    },
    "meals_add": {
        "message": "Прикрепите файл с меню или загрузите шаблон",
        "keyboard": [
            "Загрузить шаблон"
        ]
    }
}

def get_response(transition):
    value = TRANSITIONS.get(transition)
    if not value:
        raise ValueError("Переход в данное состояние не описан")
    message = value["message"]
    keyboard = None
    if value["keyboard"]:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        for k in value["keyboard"]:
            keyboard.add(KeyboardButton(k))
    else:
        keyboard = ReplyKeyboardRemove()
    return {
        "message": message,
        "keyboard": keyboard
    }
