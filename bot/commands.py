from aiogram.types import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

from bot.state import LaunchState
from model.utils import read_image, launch_calculations, get_results


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
    await call.message.answer("Start classification.")
    await call.message.answer("Please, upload your image: ")
    await LaunchState.image.set()

    await call.answer()


async def get_photo(message, state):
    await message.answer("Image was uploaded.")
    await state.update_data(image=message.photo[-1].file_id)

    response = await message.bot.download_file_by_id(message.photo[-1].file_id)

    image = await read_image(response)

    await message.answer("Inference start.")
    res = await launch_calculations(image)

    text = await get_results(res)
    await message.answer(text)

    await state.finish()


async def register_commands(dp):
    dp.register_message_handler(start, commands=["start"], state="*")
    dp.register_message_handler(menu, commands=["menu"], state="*")
    dp.register_callback_query_handler(classification, Text(equals="classification"), state="*")
    dp.register_message_handler(get_photo, content_types=['photo'], state=LaunchState.image)
