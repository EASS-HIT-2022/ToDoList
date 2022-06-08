import json


def local_db():    ### Local db
    filename = './data.json'
    with open(filename, "r+") as file:
        try:
            db_todo = json.load(file)
            return db_todo
        except:  
            db_todo = [] 
            return json.dump(db_todo,file)
