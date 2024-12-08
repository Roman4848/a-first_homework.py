from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = 'Напишите свой ключь'

bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message: types.Message):
    print("Urban message")
    await message.reply("Вы отправили специальное сообщение: Urban или ff!")


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    print("Start message")
    await message.reply("Привет! Я бот, помогающий твоему здоровью.")


@dp.message_handler()
async def all_message(message: types.Message):
    print("Мы получили сообщение")
    await message.reply("Спасибо за ваше сообщение! Напишите /start, чтобы начать.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)