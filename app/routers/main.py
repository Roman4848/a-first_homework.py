from fastapi import APIRouter
from app.models import User, Task
from app.db import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

# Получение всех пользователей
@router.get("/users")
def get_users():
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

# Получение всех задач
@router.get("/tasks")
def get_tasks():
    db: Session = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return tasks