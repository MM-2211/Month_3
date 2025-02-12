from aiogram import Dispatcher, types

# @dp.message_handler()


# @dp.message_handler(commands=["myinfo"])
async def my_info_handler(message):
    user = message.from_user
    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else "Нету"
    await message.answer(f"Hello, {user.first_name}, your ID is {user_id} and your username is {username}")

async def echo_handler(message):
    text = message.text
    await message.answer("Я вас не понимаю(")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(my_info_handler, commands="myinfo")
    dp.register_message_handler(echo_handler)