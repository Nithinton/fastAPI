from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI()

post_db = [{"id": 1, "title": "sample post"},{"id": 2, "title": "test 123", "content": "sample content", "rating": 4}]

class Post(BaseModel):
    id: int
    title: str
    content: str = None
    createdAt : datetime = datetime.now()
    rating : Optional[int] = None

@app.get("/posts")
async def getPosts():
    return {"data": post_db}

@app.get("/posts/{id}")
async def getPostById(id: int):
    for post in post_db:
        if post['id'] == id :
            return post

@app.post("/posts")
async def createPost(payload: Post):
    post_db.append(payload)
    return (post_db)