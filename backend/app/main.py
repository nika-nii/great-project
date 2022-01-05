from typing import List, Optional
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel, Field
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

DB = "course"
NEWS_COLLECTION = "news"

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
async def show_post(news_id: int):
    return news[news_id]
