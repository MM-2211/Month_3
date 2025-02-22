import asyncio

from bot_config import dp, database
from handlers import (
    start,
    other_message,
    random,
    review_dialog,
    store_fsm
)

async def main():
    start.register_handlers(dp)
    random.register_handlers(dp)
    review_dialog.register_handlers(dp)
    store_fsm.register_handlers(dp)
    other_message.register_handlers(dp)
    database.create_tables()
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())


