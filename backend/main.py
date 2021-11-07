from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

news = []
last_id = 0

@app.get("/")
async def root():
    return {"message": "Приветики"}

class PostIn(BaseModel):
    title: str
    category: str
    text: str

class Post(BaseModel):
    id: int
    title: str
    category: str
    text: str

@app.post("/news/", response_model=Post)
async def create_post(post_in: PostIn):
    global last_id
    post = Post(id = last_id, **post_in.dict())
    last_id += 1
    news.append(post)
    return post

@app.get("/news/", response_model=List[Post])
async def show_posts():
    return news

@app.get("/news/{news_id}")
async def show_post(news_id: int):
    return news[news_id]