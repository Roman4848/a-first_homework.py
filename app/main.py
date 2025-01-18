import logging
from fastapi import FastAPI
from app.db import engine
from app.models import Base
from app.routers import main as routers

# Настройка логирования
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Подключение маршрутов
app.include_router(routers.router)