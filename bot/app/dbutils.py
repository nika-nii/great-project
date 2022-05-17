from pymongo import MongoClient
import logging

MONGO_HOST = "mongo"
MONGO_PORT = 27017
MONGO_DB = "bot"

mongo_client = MongoClient(MONGO_HOST, MONGO_PORT)
db = mongo_client[MONGO_DB]

def get_state(chat_id):
    states = db["states"]
    state = states.find_one({"chat_id": chat_id})
    return state["state"]

def set_state(chat_id, state):
    states = db["states"]
    current_state = states.find_one({"chat_id": chat_id})
    logging.debug(f"Found state: {current_state}")
    if current_state:
        states.update_one({"chat_id": chat_id}, { "$set": {"state": state}})
    else:
        states.insert_one({"chat_id": chat_id, "state": state})

def set_state_document(chat_id, document_id):
    states = db["states"]
    states.update_one({"chat_id": chat_id}, { "$set": {"document_id": document_id}})

def get_state_document(chat_id):
    states = db["states"]
    state = states.find_one({"chat_id": chat_id})
    return state["document_id"]
    
def get_system_user(tg_user_id):
    users = db["users"]
    user = users.find_one({"tg_user_id": tg_user_id})
    return user

def get_user_by_token(registration_token):
    users = db["users"]
    user = users.find_one({"registration_token": registration_token})
    return user

def link_user_to_tg(user_id, tg_user_id):
    users = db["users"]
    users.update_one({"_id": user_id}, { "$set": {"tg_user_id": tg_user_id}})

def create_admin(tg_user_id):
    users = db["users"]
    users.insert_one({"tg_user_id": tg_user_id, "registration_token": "admin", "role": "admin"})

def create_user(role, token):
    users = db["users"]
    users.insert_one({"role": role, "registration_token": token})

def news_create():
    news = db["news"]
    id = news.insert_one({
            "title": "",
            "category": "",
            "text": ""
        }).inserted_id
    return id

def news_add_title(id, title):
    news = db["news"]
    news.update_one({"_id": id}, { "$set": {"title": title}})

def news_add_category(id, category):
    news = db["news"]
    news.update_one({"_id": id}, { "$set": {"category": category}})

def news_add_text(id, text):
    news = db["news"]
    news.update_one({"_id": id}, { "$set": {"text": text}})

def news_get(id):
    news = db["news"]
    return news.find_one({"_id": id})