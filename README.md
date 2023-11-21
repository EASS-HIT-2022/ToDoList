# ToDo List App

### FastAPI for Backend and Streamlit for Frontend

## Table of Contents
- [Installation](#installation)
- [Features](#features)
  - [Backend](#backend)
  - [Frontend](#frontend)
  - [Database](#database)
  - [Docker-compose](#Docker-compose)
- [To Be Added](#to-be-added)
- [Screens and Preview](#screens-and-preview)
- [Testing](#testing)
- [Author](#Author)

---

## Installation

To run the ToDo List App, use Docker with docker-compose:

Run the following command in your terminal: ``docker-compose -d --build``

Access the app at: [http://127.0.0.1:7000/](http://127.0.0.1:7000/)

Access the backend API at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Features

- Database powered by Redis for high performance.
- FastAPI for the backend, implementing CRUD operations (refer to the backend readme for more details).
- Streamlit for a user-friendly frontend interface.
- Docker-compose to seamlessly integrate all services.
- Backend unit tests for robust functionality.

### Backend

Utilizing FastAPI for efficient backend development.

### Frontend

Employing Streamlit for a clean and intuitive frontend experience.

### Database

The app utilizes Redis, serving as an in-memory data structure store, distributed key–value database, cache, and message broker with optional durability.

### Docker-compose

1. Backend (FastAPI)
2. Frontend (Streamlit)
3. Database (Redis)

---

## To Be Added

- [x] Third Redis service.
- [x] Implementation of tests.
- [ ] Consideration for additional features.

---

## Screens and Preview

### API (Via FastAPI)
![API](https://github.com/EASS-HIT-2022/ToDoList/blob/main/Screenshots/brave_atOjo8emnK.png)

#### Create a Task:
![Create Task](https://github.com/EASS-HIT-2022/ToDoList/blob/main/Screenshots/J4upY5kiMA.gif)

#### Delete a Task:
![Delete Task](https://github.com/EASS-HIT-2022/ToDoList/blob/main/Screenshots/UZfgFffn7X.gif)

#### Update a Task:
![Update Task](https://github.com/EASS-HIT-2022/ToDoList/blob/main/Screenshots/1a1gkQV89w.gif)

---

## Testing

1. Comment in backend/main.py lines 6 & 7 and uncomment lines 10 & 11.
2. Run this command: `docker-compose run --service-ports backend bash`
3. Run: `pytest`
#### Results:
![Results](https://github.com/EASS-HIT-2022/ToDoList/blob/main/Screenshots/Code_FN2dXEepdB.png)


## Author

- [Itai Markovetzky](https://github.com/itai-markovetzky)

Feel free to reach out if you have any questions or feedback. Contributions are welcome!


