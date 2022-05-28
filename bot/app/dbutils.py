from pymongo import MongoClient
import logging
from enum import Enum

MONGO_HOST = "mongo"
MONGO_PORT = 27017
MONGO_DB = "bot"

class States(Enum):
    START="start"
    MENU="menu"

class Roles(Enum):
    ADMIN="admin"
    EDITOR="editor"

mongo_client = MongoClient(MONGO_HOST, MONGO_PORT)
db = mongo_client[MONGO_DB]
states = db["states"]
users = db["users"]

def get_state(client_id: int) -> States:
    '''Получение текущего состояния клиента'''
    state = states.find_one(
        filter={"client_id": client_id}
    )
    return State(state["state"])

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
    return state["context"]

def update_context(client_id: int, value: dict):
    '''Обновление контекста. value - словарь с обновляемыми значениями'''
    states.update_one(
        filter={"client_id": client_id},
        update={"$set": value},
        upsert=True
    )

def get_user_by_telegram_id(telegram_id: int) -> int:
    '''Получение системного ID пользователя по ID в телеграме'''
    user = users.find_one(
        filter={"telegram_id": telegram_id}
    )
    return user

def get_user_by_token(token: str) -> int:
    '''Получение системного ID пользователя по токену приглашения'''
    user = users.find_one(
        filter={"token": token}
    )
    return user

def add_telegram_id_to_user(user_id: int, telegram_id: int):
    '''Добавить Telegram ID к ID пользователя'''
    users.update_one(
        filter={"user_id": user_id},
        update={"$set": {"telegram_id": telegram_id}}
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