from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

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
main_kb.add(button_calculate).add(button_info).add(button_buy)


inline_kb = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(button_calories, button_formulas)


inline_buy_kb = InlineKeyboardMarkup()
button_product1 = InlineKeyboardButton(text='Продукт 1', callback_data='product1')
button_product2 = InlineKeyboardButton(text='Продукт 2', callback_data='product2')
button_product3 = InlineKeyboardButton(text='Продукт 3', callback_data='product3')
button_product4 = InlineKeyboardButton(text='Продукт 4', callback_data='product4')
inline_buy_kb.add(button_product1, button_product2, button_product3, button_product4)


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

    # Отправляем изображения продуктов
    await message.answer_photo(photo=open('files/product1.png', 'rb'),
                               caption="Название: Product1\nОписание: Описание 1\nЦена: 100")
    await message.answer_photo(photo=open('files/product2.png', 'rb'),
                               caption="Название: Product2\nОписание: Описание 2\nЦена: 200")
    await message.answer_photo(photo=open('files/product3.png', 'rb'),
                               caption="Название: Product3\nОписание: Описание 3\nЦена: 300")
    await message.answer_photo(photo=open('files/product4.png', 'rb'),
                               caption="Название: Product4\nОписание: Описание 4\nЦена: 400")


    await message.answer("Выберите продукт, нажав на кнопку ниже:", reply_markup=inline_buy_kb)


@dp.callback_query_handler(text='product1')
async def buy_product1(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.callback_query_handler(text='product2')
async def buy_product2(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.callback_query_handler(text='product3')
async def buy_product3(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.callback_query_handler(text='product4')
async def buy_product4(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer(
        "Используйте команду /start, чтобы начать, или нажмите 'Рассчитать', чтобы получить информацию о норме калорий.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)