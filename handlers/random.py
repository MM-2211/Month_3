import random
from aiogram import Dispatcher, types

names = ("Carvajal", "Ramos", "Varan", "Marcelo")


# @dp.message_handler(commands=["random"])
async def random_name_handler(message):
    random_name = random.choice(names)
    await message.answer(random_name)

def register_handlers(dp):
    dp.register_message_handler(random_name_handler, commands="random")