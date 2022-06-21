import boto3

from aiogram.types import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from bot.config import S3_KEY, S3_SECRET_KEY, BUCKET_NAME


async def set_commands(bot):
    commands = [
        BotCommand(command="/menu", description="Menu"),
    ]
    await bot.set_my_commands(commands)


async def start(message):
    hi_message = "Welcome to the Сar Recognition Bot."

    await message.answer(hi_message)
    await menu(message)


async def menu(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Classification", callback_data="classification"))

    await message.answer(text="You can choose what interests you:", reply_markup=keyboard)


async def classification(call):
    await call.message.answer("start classification")

    await call.answer()


async def register_commands(dp):
    dp.register_message_handler(start, commands=["start"], state="*")
    dp.register_message_handler(menu, commands=["menu"], state="*")
    dp.register_callback_query_handler(classification, Text(equals="classification"), state="*")
