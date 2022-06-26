import json
import redis

def local_db():    ### Local db
    filename = './data.json'
    with open(filename, "r+") as file:
        try:
            db_todo = json.load(file)
            return db_todo
        except:  
            db_todo = [] 
            return json.dump(db_todo,file)


def convertor(data):
    if isinstance(data, bytes):  return data.decode('ascii')
    if isinstance(data, dict):   return dict(map(convertor, data.items()))
    if isinstance(data, tuple):  return map(convertor, data)
    return data

redis_con = redis.StrictRedis(host='docker.for.mac.localhost', port=6379)

try:
    redis_con.ping()
    print('Connected to redis')
except:
    print('Connect to redis failed')

