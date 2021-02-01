from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import locations_buttons
from loader import dp


@dp.message_handler(Command("show_on_map"))
async def show_on_map(message: types.Message):
    await message.answer(f"Хай, {message.from_user.full_name}! \n"
                         f"Узнать координаты",
                         reply_markup=locations_buttons.keyboard)


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def get_location(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    await message.answer(f"latitude = {latitude}"
                         f"longitude = {longitude}",
                         disable_web_page_preview=True,
                         reply_markup=ReplyKeyboardRemove())
    await message.answer_location(latitude=latitude,
                                  longitude=longitude)