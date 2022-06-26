from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional, List

import redis
from models import Todo
from database import local_db, redis_con, convertor

# Just for testting
# from .models import Todo
# from .database import local_db, redis_con, convertor

import json

import uvicorn

app = FastAPI(title="To-do List API")

#This will make a List of Todo
class todos(BaseModel):
    todo_name: List[Todo]


store_todo = [] #todos(todo_name = [])


# Create, Read, Update, Delete

@app.get('/')
async def home():
    return {"Hello": "World"}

@app.post('/todo/')
async def create_todo(todo: Todo):
    todo_dict = todo.dict()
    redis_con.hmset(todo_dict.get('title'), todo.dict())

    return store_todo

@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    store_todo_redis = list()
    list_key = [data.decode('ascii') for data in convertor(redis_con.keys())]
    for key in list_key:
        row = redis_con.hgetall(key)
        row = convertor(row)
        store_todo_redis.append(row)

    return store_todo_redis

@app.get('/todo/{title}')
async def get_todo(title: str):
    store_todo_redis = list()
    list_key = [data.decode('ascii') for data in convertor(redis_con.keys())]
    for key in list_key:
        row = redis_con.hgetall(key)
        row = convertor(row)
        store_todo_redis.append(row)
    
    return {}

        

@app.put('/todo/{title}')
async def update_todo(title: str, todo: Todo):

    if redis_con.hgetall(title):
        # update value in here
        if title == todo.title:
            redis_con.hset(title, 'description', todo.description)
            redis_con.hset(title, 'due_date', todo.due_date)

    return todo.dict()
    


@app.delete('/todo/{title}')
async def delete_todo(title: str):

    # get a value given a key
    if redis_con.hgetall(title):
        # Delete a row given hash key
        redis_con.delete(title)
    
    store_todo_redis = list()
    list_key = [data.decode('ascii') for data in convertor(redis_con.keys())]
    for key in list_key:
        row = redis_con.hgetall(key)
        row = convertor(row)
        store_todo_redis.append(row)
    
    return {}
    

if __name__ == "__main__":
    uvicorn.run(app)
