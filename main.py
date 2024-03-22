from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI()

class PostRequestDTO(BaseModel):
    title: str
    content: str
    createdAt : datetime = datetime.now()
    # rating : int = None 
    # This means that if rating is not provided when creating an instance of the model, it will default to None. 
    # However, once the instance is created, rating must be an integer and cannot be None
    rating : Optional[int] = None

@app.get("/")
async def home():
    return {"message": "hello world"}

@app.post("/createpost")
async def createPost(payload: PostRequestDTO):
    print(payload)
    return (payload)