# ToDo List App
### FastAPI for backend and Streamlit for frontend
-------
## Installation
#### Run Docker (With docker-compose)
 `docker-compose -d --build`

**In order to go to the app itself head to:**
`http://127.0.0.1:7000/`

**In order to go to the backend API head to:**
`http://127.0.0.1:8000/`

-------
## Features

- Database is via File. (deprecated)
- Database is redis for highly performance
- FastAPI for the backend CRUD based. (more info on the backend readme)
- Streamlit neat interface for the frontline.
- Docker-compose to fit together all of the services.
- Backend unit tests.
------

### Backend
Using FastAPI for the backend side

### Frontend
Using Streamlit neat interface for the frontend

### Database
Using Redis, Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability.

### Docker-compose
1. Backend (FastAPI)
2. Frontend (Streamlit)
3. Database (Redis)

## To Be added
- [x] Third redis service.
- [x] Tests.
- [ ] Maybe some more features.
-----
## Screens and Preview

#### Create a Task:
![](https://i.imgur.com/VaI3iA4.gif)

#### Delete a task:
![](https://puu.sh/J57nP/9b99ea7e29.gif)

#### Update a task:
![](https://puu.sh/J57oA/1273a1023d.gif)

-------
## Testing
1. Comment in backend/main.py lines 6 & 7 and uncomment lines 10 & 11.
2. run this command: `docker-compose run --service-ports backend bash`
3. last but not least, run: `pytest`
4. ![Results](https://puu.sh/J83Rx/8fcbdfb95f.png)
