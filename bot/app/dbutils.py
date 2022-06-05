from pymongo import MongoClient
import logging
from enum import Enum

MONGO_HOST = "mongo"
MONGO_PORT = 27017
MONGO_DB = "bot"

class States(Enum):
    START="start"
    MENU="menu"
    REGISTRATION="registration"
    USER_ADD="user_add"
    USER_NAME="user_name"
    NEWS_ADD="news_add"
    NEWS_CATEGORY="news_category"
    NEWS_BODY="news_body"
    DOCUMENT_ADD="document_add"
    DOCUMENT_BODY="document_body"
    MEALS_ADD="meals_add"


class Roles(Enum):
    ADMIN="Администратор"
    EDITOR="Редактор"

mongo_client = MongoClient(MONGO_HOST, MONGO_PORT)
db = mongo_client[MONGO_DB]
states = db["states"]
users = db["users"]

def get_state(client_id: int) -> States:
    '''Получение текущего состояния клиента'''
    state = states.find_one(
        filter={"client_id": client_id}
    )
    return States(state.get("state", States.START.value))

def set_state(client_id: int, state: States):
    '''Установка состояния клиента'''
    states.update_one(
        filter={"client_id": client_id},
        update={ "$set": {"state": state.value}},
        upsert=True
    )

def get_context(client_id: int) -> dict:
    '''Получение контекста (контекст = редактируемый документ и т.д.)'''
    state = states.find_one(
        filter={"client_id": client_id}
    )
    return state.get("context", {})

def update_context(client_id: int, value: dict):
    '''Обновление контекста. value - словарь с обновляемыми значениями'''
    old_context = get_context(client_id)
    new_context = old_context | value
    states.update_one(
        filter={"client_id": client_id},
        update={"$set": {"context": new_context}},
        upsert=True
    )

def get_user_by_telegram_id(telegram_id: int) -> int:
    '''Получение системного ID пользователя по ID в телеграме'''
    user = users.find_one(
        filter={"telegram_id": telegram_id}
    )
    if user:
        return user["_id"]
    else:
        return None

def get_user_by_token(token: str) -> int:
    '''Получение системного ID пользователя по токену приглашения'''
    user = users.find_one(
        filter={"token": token}
    )
    if user:
        return user["_id"]
    else:
        return None

def add_telegram_id_to_user(user_id: int, telegram_id: int):
    '''Добавить Telegram ID к ID пользователя'''
    users.update_one(
        filter={"_id": user_id},
        update={"$set": {"telegram_id": telegram_id}}
    )

def get_user_name(user_id: int) -> str:
    '''Получить имя системного пользователя'''
    user = users.find_one(
        filter={"_id": user_id}
    )
    return user.get("name", "Без имени")

def get_user_role(user_id: int) -> Roles:
    '''Получить роль системного пользователя'''
    user = users.find_one(
        filter={"_id": user_id}
    )
    return Roles(user.get("role", Roles.EDITOR.value))

def set_user_role(user_id: int, role: Roles):
    '''Установить роль для пользователя'''
    users.update_one(
        filter={"_id": user_id},
        update={"$set": {"role": role.value}}
    )

def create_user(name: str, role: Roles, token: str) -> int:
    '''Создать пользователя в БД'''
    return users.insert_one(
        {
            "name": name,
            "role": role.value,
            "token": token
        }
    ).inserted_id