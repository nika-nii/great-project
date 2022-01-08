from typing import List, Optional
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel, Field
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
import datetime

DB = "course"
NEWS_COLLECTION = "news"
DOCS_COLLECTION = "docs"
MEALS_COLLECTION = "meals"

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

news = []
last_id = 0

@app.get("/")
async def root():
    return {"message": "Приветики"}

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

class Post(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id") #мб str или ничем
    title: str
    category: str
    text: str
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class Doc(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    title: str
    type: str
    file_path: str
    author: str
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class Breakfast(BaseModel):
    hot_meal: str
    hot_drink: str
    fruit: str
    milk: str
    bakery: str

class Dinner(BaseModel):
    hot_meal_first: str
    hot_meal_second: str
    hot_drink: str
    snack_one: str
    snack_two: str
    bread: str
    drink: str

class Meal(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    date: datetime.datetime
    breakfast: Breakfast
    dinner: Dinner
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

@app.post("/news/")
async def create_post(post_in: Post):
    with MongoClient() as client:
        collection = client[DB][NEWS_COLLECTION]
        if (hasattr(post_in, "id")):
            delattr(post_in, "id")
        result = collection.insert_one(post_in.dict(by_alias=True))
        res_id = result.inserted_id
        res_obj = collection.find_one(res_id)
        print(res_obj)
        post_in.id = res_id
        return {"post_in": post_in}
        # return Post(id = str(res_obj.id), title = res_obj.title, category = res_obj.title, text = res_obj.text)

@app.get("/news/", response_model=List[Post])
async def show_posts():
    with MongoClient() as client:
        collection = client[DB][NEWS_COLLECTION]
        news_list = collection.find()
        pretty_list = []
        for news in news_list:
            pretty_list.append(Post(**news))
        return pretty_list

@app.get("/news/{news_id}")
async def show_post(news_id: PyObjectId):
    with MongoClient() as client:
        collection = client[DB][NEWS_COLLECTION]
        item = collection.find_one({"_id": news_id})
        return Post(**item)

@app.post("/docs/")
async def create_doc(doc_in: Doc):
    with MongoClient() as client:
        collection = client[DB][DOCS_COLLECTION]
        if (hasattr(doc_in, "id")):
            delattr(doc_in, "id")
        result = collection.insert_one(doc_in.dict(by_alias=True))
        res_id = result.inserted_id
        res_obj = collection.find_one(res_id)
        print(res_obj)
        doc_in.id = res_id
        return {"doc_in": doc_in}

@app.get("/docs/", response_model=List[Doc])
async def show_docs():
    with MongoClient() as client:
        collection = client[DB][DOCS_COLLECTION]
        docs_list = collection.find()
        pretty_list = []
        for docs in docs_list :
            pretty_list.append(Doc(**docs))
        return pretty_list

@app.get("/docs/{docs_id}")
async def show_doc(docs_id: PyObjectId):
    with MongoClient() as client:
        collection = client[DB][DOCS_COLLECTION]
        item = collection.find_one({"_id": docs_id})
        return Doc(**item)

@app.post("/meals/")
async def create_meal(meal_in: Meal):
    with MongoClient() as client:
        collection = client[DB][MEALS_COLLECTION]
        if (hasattr(meal_in, "id")):
            delattr(meal_in, "id")
        result = collection.insert_one(meal_in.dict(by_alias=True))
        res_id = result.inserted_id
        res_obj = collection.find_one(res_id)
        print(res_obj)
        meal_in.id = res_id
        return {"meal_in": meal_in}

@app.get("/meals/{meal_id}")
async def show_meal(meal_id: PyObjectId):
    with MongoClient() as client:
        collection = client[DB][MEALS_COLLECTION]
        item = collection.find_one({"_id": meal_id})
        return Meal(**item)