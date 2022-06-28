import asyncio
import logging

from aiogram import Bot, Dispatcher
from bot import config
from bot.commands import set_commands, register_commands

from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Create a new instance of the preferred reporting system.
logger = logging.getLogger("bot")


async def main():
    bot = Bot(token=config.BOT_TOKEN)

    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    await set_commands(bot)

    await register_commands(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
