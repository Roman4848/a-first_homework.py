from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = 'Напишите свой ключь'

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создание клавиатуры
kd = ReplyKeyboardMarkup(resize_keyboard=True)  # resize_keyboard для адаптации размера
button_calculate = KeyboardButton(text='Рассчитать')
button_info = KeyboardButton(text='Информация')
kd.add(button_calculate).add(button_info)  # Добавление кнопок на клавиатуру

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Используйте кнопки ниже:", reply_markup=kd)  # Используем созданную клавиатуру

@dp.message_handler(text='Привет!')
async def greet(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

@dp.message_handler(text='Рассчитать')
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()  # Устанавливаем состояние age

@dp.message_handler(text='Информация')
async def inform(message: types.Message):
    await message.answer('Информация о боте!')

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await message.answer("Введите свой рост (в см):")
    await UserState.growth.set()  # Устанавливаем состояние growth

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await message.answer("Введите свой вес (в кг):")
    await UserState.weight.set()  # Устанавливаем состояние weight

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес
    data = await state.get_data()

    # Формула
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.finish()  # Завершение состояний

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)