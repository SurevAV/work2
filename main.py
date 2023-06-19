import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import db
import handlers
from data.config import Config


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(Config.BOT_TOKEN, validate_token=True)


    bot['db'] = await db.setup()

    dp = Dispatcher(bot, storage=MemoryStorage())
    handlers.user.setup(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


