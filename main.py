from fastapi import FastAPI, Response, status, HTTPException
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
async def getPostById(id: int, response : Response):
    
    for post in post_db:
        if post['id'] == id :
            return post
        else: 
            #response.status_code = status.HTTP_404_NOT_FOUND
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post id: {id} not found.") # good approach
            #return "id not found"

@app.post("/posts", status_code = status.HTTP_201_CREATED)
async def createPost(payload: Post):
    print(status.HTTP_201_CREATED)
    post_db.append(payload)
    return ({"data": payload.dict()})

