from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Импортируйте ваши модели здесь, если они есть
from .user import User  # Пример импорта модели User
from .task import Task  # Пример импорта модели Task