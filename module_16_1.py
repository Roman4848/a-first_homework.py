from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{id}")
async def read_user(id: int):
    return {"message": f"Вы вошли как пользователь № {id}"}

@app.get("/user")
async def read_user_query(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}