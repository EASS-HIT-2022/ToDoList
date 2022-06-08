from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional, List
from models import Todo
from database import local_db
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
    with open("./data.json", "r") as file:
        store_todo = json.load(file)

    store_todo.append(todo.dict())

    with open("./data.json", "w") as file:
        json.dump(store_todo,file)
    return store_todo

@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    with open("./data.json", "r") as file:
        store_todo = json.load(file)
    return store_todo

@app.get('/todo/{title}')
async def get_todo(title: str):
    with open("./data.json", "r") as file:
        store_todo = json.load(file)
    
    for task in store_todo:
        for attribute, value in task.items():
            if attribute == "title":
                if value == title:
                    return task
    return {}

        

@app.put('/todo/{title}')
async def update_todo(title: str, todo: Todo):
    with open("./data.json", "r") as file:
        store_todo = json.load(file)
    for task in store_todo:
        for attribute, value in task.items():
            if attribute == "title":
                if value == todo.title:
                    task['description'] = todo.description
                    task['due_date'] = todo.due_date
    with open("./data.json", "w") as file:
        json.dump(store_todo,file)
    return store_todo
    


@app.delete('/todo/{title}')
async def delete_todo(title: str):

    with open("./data.json", "r") as file:
        store_todo = json.load(file)
    store_todo2 = []
    for task in store_todo:
        for attribute, value in task.items():
            if attribute == "title":
                 if value != title:
                    store_todo2.append(task)
    with open("./data.json", "w") as file:
         json.dump(store_todo2,file)
    return store_todo2
    


if __name__ == "__main__":
    uvicorn.run(app)
