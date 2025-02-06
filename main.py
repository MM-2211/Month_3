import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup
from dotenv import dotenv_values

token = dotenv_values(".env").get("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher(bot)

names = ("Carvajal", "Ramos", "Varan", "Marcelo")

@dp.message_handler(commands=["start"])
async def start_handler(message):
    user = message.from_user
    await message.answer(f"Hello, {user.first_name}!")

@dp.message_handler(commands=["myinfo"])
async def my_info_handler(message):
    user = message.from_user
    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else "Нету"
    await message.answer(f"Hello, {user.first_name}, your ID is {user_id} and your username is {username}")

@dp.message_handler(commands=["random"])
async def random_name_handler(message):
    random_name = random.choice(names)
    await message.answer(random_name)

@dp.message_handler()
async def echo_handler(message):
    text = message.text
    await message.answer(text)

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())


