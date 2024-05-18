from fastapi import FastAPI
from function import *

app = FastAPI()

@app.get("/get_message")
async def get_message():
    return {"message": "This is the first API"}

@app.get("/get_data")
async def get_data():
    data = getdata()
    return {"data": data}

@app.post("/postData")
async def post_data(data: dict):
    name = data.get("name")
    UserName = data.get("UserName")
    Password = data.get("Password")
    insert_data_into_table(name, UserName, Password)
    return {"message": "Data inserted successfully"}

@app.get("/get_data/{id}")
async def get_data(id: int):
    data = fetch_data_from_user_id(id)
    return {"data": data}
