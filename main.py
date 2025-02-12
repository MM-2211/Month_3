import asyncio

from bot_config import dp
from handlers import (
    start,
    other_message,
    random,
    review_dialog
)

async def main():
    start.register_handlers(dp)
    random.register_handlers(dp)
    review_dialog.register_handlers(dp)
    other_message.register_handlers(dp)
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())


