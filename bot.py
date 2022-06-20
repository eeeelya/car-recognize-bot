import asyncio
import logging
import asyncpg

from aiogram import Bot, Dispatcher, executor, types
from bot import config
from bot.commands import set_commands, register_commands

# Create a new instance of the preferred reporting system.
logger = logging.getLogger("bot")


async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher(bot)

    pool = await asyncpg.create_pool(
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        host=config.POSTGRES_HOST,
        database=config.POSTGRES_DB,
        command_timeout=60,
    )

    # await create_tables(pool)

    await set_commands(bot)

    # dp.middleware.setup(DbMiddleware(pool))
    # dp.middleware.setup(ThrottlingMiddleware())

    await register_commands(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
