from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class PostRequestDTO(BaseModel):
    title: str
    content: str
    createdAt : datetime = datetime.now()

@app.get("/")
async def home():
    return {"message": "hello world"}

@app.post("/createpost")
async def createPost(payload: PostRequestDTO):
    print(payload)
    return (payload)