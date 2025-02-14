from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import Database

token = dotenv_values(".env").get("BOT_TOKEN")
bot = Bot(token=token)
storage = MemoryStorage()
database = Database("database.db")
dp = Dispatcher(bot, storage=storage)