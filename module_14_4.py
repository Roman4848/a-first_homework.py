from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os
from crud_functions import initiate_db, get_all_products
import sqlite3

api = 'Напишите свой ключь'

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton(text='Рассчитать')
button_info = KeyboardButton(text='Информация')
button_buy = KeyboardButton(text='Купить')
main_kb.add(button_calculate, button_info, button_buy)

inline_kb = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(button_calories, button_formulas)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=main_kb)


@dp.message_handler(text='Информация')
async def inform(message: types.Message):
    await message.answer('Информация о боте!')


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.answer()
    formula_message = (
        "Формула Миффлина-Сан Жеора:\n"
        "Для мужчин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5\n"
        "Для женщин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161"
    )
    await call.message.answer(formula_message)


@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.finish()


@dp.message_handler(text='Купить')
async def buying_menu(message: types.Message):
    await message.answer("Вот все доступные продукты:")


    products = get_all_products()


    if not products:
        await message.answer("Нет доступных продуктов.")
        return


    inline_buy_kb = InlineKeyboardMarkup()


    for product in products:
        title, description, price = product
        await message.answer_photo(photo=open(f'files/{title}.png', 'rb'),
                                   caption=f"Название: {title}\nОписание: {description}\nЦена: {price}")

        inline_buy_kb.add(InlineKeyboardButton(text=f"Купить {title}", callback_data=f'buy_{title}'))

    await message.answer("Выберите продукт, нажав на кнопку ниже:", reply_markup=inline_buy_kb)


@dp.callback_query_handler(lambda c: c.data.startswith('buy_'))
async def buy_product(call: types.CallbackQuery):
    product_name = call.data.split('_')[1]
    await call.answer()
    await call.message.answer(f"Вы успешно приобрели продукт: {product_name}!")


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer(
        "Используйте команду /start, чтобы начать, или нажмите 'Рассчитать', чтобы получить информацию о норме калорий.")


if __name__ == '__main__':

    initiate_db()


    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()


    cursor.execute("SELECT COUNT(*) FROM Products")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       ('Product1', 'Описание 1', 100))
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       ('Product2', 'Описание 2', 200))
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       ('Product3', 'Описание 3', 300))
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       ('Product4', 'Описание 4', 400))
        conn.commit()

    conn.close()

    executor.start_polling(dp, skip_updates=True)