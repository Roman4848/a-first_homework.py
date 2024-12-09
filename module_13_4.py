from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = 'Напишите свой ключь'

bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью. Используйте команду /calories для расчета нормы калорий.")

# Функция для установки возраста
@dp.message_handler(commands=['calories'])
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

# Функция для установки роста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await UserState.growth.set()

# Функция для установки веса
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await UserState.weight.set()

# Функция для расчета и отправки нормы калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    # Примерная формула для расчета калорий (для мужчин)
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.finish()  # Завершение состояний


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Используйте команду /calories для расчета нормы калорий.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
