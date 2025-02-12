from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()


async def start_dialog(callback: CallbackQuery):
    await RestourantReview.name.set()
    await callback.message.answer("Как вас зовут?")

async def process_name(message: Message, state: FSMContext):
    await RestourantReview.next()
    await message.answer("Какой ваш номер телефона?")

async def process_phone_number(message: Message, state: FSMContext):
    phone_num = message.text
    if phone_num.isdigit():
        await RestourantReview.next()
        await message.answer("Поставьте оценку от 1 до 5")
    else:
        await message.answer("Номер состоит из цифр, гений")

async def process_rate(message: Message, state: FSMContext):
    rate_client = message.text
    if rate_client.isdigit() and 1 <= int(rate_client) <= 5:
        await RestourantReview.next()
        await message.answer("Укажите вашу жалобу")
    else:
        await message.answer("Нужна оценка от 1 до 5, алло!")

async def process_extra_comments(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Спасибо за отзыв!")

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_dialog,lambda c: c.data == "review")
    dp.register_message_handler(process_name, state=RestourantReview.name)
    dp.register_message_handler(process_phone_number, state=RestourantReview.phone_number)
    dp.register_message_handler(process_rate, state=RestourantReview.rate)
    dp.register_message_handler(process_extra_comments, state=RestourantReview.extra_comments)