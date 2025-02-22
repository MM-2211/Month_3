from aiogram import Dispatcher
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


# @dp.message_handler(commands=["start"])
async def start_handler(message: Message):
    user = message.from_user
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Наш адрес", callback_data="ouraddress"),
                InlineKeyboardButton(text="Контакты", callback_data="contacts")
            ],
            [
                InlineKeyboardButton(text="Режим работы", callback_data="timework"),
                InlineKeyboardButton(text="Наш сайт", url="https://www.chess.com/play")
            ],
            [
                InlineKeyboardButton(text="Оставить жалобу", callback_data="review")
            ]
        ]
    )
    await message.answer(f"Hello, {user.first_name}!", reply_markup=kb)

async def our_address_handler(callback: CallbackQuery):
    await callback.message.answer("Жибек-Жолу 95А")

async def contacts_handler(callback: CallbackQuery):
    await callback.message.answer("Наши контакты 0312435923")

async def time_work_handler(callback: CallbackQuery):
    await callback.message.answer("С 8:00 am до 1:00 pm")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_callback_query_handler(our_address_handler, lambda c: c.data == "ouraddress")
    dp.register_callback_query_handler(contacts_handler, lambda c: c.data == "contacts")
    dp.register_callback_query_handler(time_work_handler, lambda c: c.data == "timework")