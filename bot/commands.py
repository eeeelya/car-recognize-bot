from aiogram.types import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text


async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="Мой профиль"),
    ]
    await bot.set_my_commands(commands)


async def start(message):
    hi_message = "Welcome to the Сar Recognition Bot. You can choose what interests you:"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Classification", callback_data="classification"))
    keyboard.add(InlineKeyboardButton(text="All launches", callback_data="all_launches"))

    await message.answer(hi_message, reply_markup=keyboard)


async def classification(call):
    await call.message.answer("start classification")
    await call.answer()


async def all_launches(call):
    await call.message.answer("all_launches")
    await call.answer()


async def register_commands(dp):
    dp.register_message_handler(start, commands=["start"], state="*")
    dp.register_callback_query_handler(classification, Text(equals="classification"), state="*")
    dp.register_callback_query_handler(all_launches, Text(equals="all_launches"), state="*")
