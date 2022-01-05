from typing import List, Optional
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
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

class Post(BaseModel):
    id: Optional[ObjectId()] #мб str или ничем
    title: str
    category: str
    text: str

@app.post("/news/", response_model=Post)
async def create_post(post_in: Post):
    with MongoClient() as client:
        collection = client[DB][NEWS_COLLECTION]
        result = collection.insert_one(post_in.dict())
        res_id = result.inserted_id
        res_obj = collection.find_one(res_id)
        print(res_obj)
        return Post(id = str(res_obj.id), title = res_obj.title, category = res_obj.title, text = res_obj.text)

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
