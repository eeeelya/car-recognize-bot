import os
import logging
import asyncio
import psycopg2
import asyncpg

from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create a new instance of the preferred reporting system.
logger = logging.getLogger("bot")

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

connection = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host="db", port=5432)

cursor = connection.cursor()


@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.answer("Test 1")
    cursor.execute("SELECT id, model, price from mobile")
    rows = cursor.fetchall()
    for row in rows:
        await message.answer(row[0])
        await message.answer(row[1])
        await message.answer(row[2])

    message.from_user


def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)


    try:
        executor.start_polling(dispatcher=dp, skip_updates=True)
    finally:
        connection.close()


if __name__ == '__main__':
    asyncio.run(main())
