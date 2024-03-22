from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()


@app.get("/")
async def home():
    return {"message": "hello world"}

@app.post("/createpost")
async def createPost(payload: dict = Body(...)):
    return (payload)