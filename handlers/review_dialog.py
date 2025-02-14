from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from bot_config import database

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()


async def start_dialog(callback: CallbackQuery):
    await RestourantReview.name.set()
    await callback.message.answer("Как вас зовут?")

async def process_name(message: Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data['name'] = name
    await RestourantReview.next()
    await message.answer("Какой ваш номер телефона?")

async def process_phone_number(message: Message, state: FSMContext):
    phone_number = message.text
    async with state.proxy() as data:
        data['phone_number'] = phone_number
    await RestourantReview.next()
    await message.answer("Поставьте оценку от 1 до 5")

async def process_rate(message: Message, state: FSMContext):
    rate = message.text
    if rate.isdigit() and 1 <= int(rate) <= 5:
        async with state.proxy() as data:
            data['rate'] = rate
        await RestourantReview.next()
        await message.answer("Укажите вашу жалобу")
    else:
        await message.answer("Нужна оценка от 1 до 5, алло!")

async def process_extra_comments(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["extra_comments"] = message.text
    # print(data)
    database.add_review(data)
    await message.answer("Спасибо за отзыв!")
    await state.finish()



def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_dialog,lambda c: c.data == "review")
    dp.register_message_handler(process_name, state=RestourantReview.name)
    dp.register_message_handler(process_phone_number, state=RestourantReview.phone_number)
    dp.register_message_handler(process_rate, state=RestourantReview.rate)
    dp.register_message_handler(process_extra_comments, state=RestourantReview.extra_comments)