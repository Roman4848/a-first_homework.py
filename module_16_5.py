from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Папка для шаблонов
templates = Jinja2Templates(directory="templates")

# Пустой список пользователей
users: List['User '] = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "users": [user]})
    raise HTTPException(status_code=404, detail="User  not found")

@app.post("/user/", response_model=User )
async def create_user(user: User):
    user_id = len(users) + 1  # ID будет на 1 больше, чем количество пользователей
    new_user = User(id=user_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}", response_model=User )
async def update_user(user_id: int, user: User):
    for existing_user in users:
        if existing_user.id == user_id:
            existing_user.username = user.username
            existing_user.age = user.age
            return existing_user
    raise HTTPException(status_code=404, detail="User  not found")

@app.delete("/user/{user_id}", response_model=User )
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User  not found")

# Создание нескольких пользователей
@app.on_event("startup")
async def startup_event():
    users.append(User(id=1, username="UrbanUser ", age=24))
    users.append(User(id=2, username="UrbanTest", age=22))
    users.append(User(id=3, username="Capybara", age=60))