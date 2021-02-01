from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer("Меню", reply_markup=menu)


@dp.message_handler(text="Кнопка №1")
async def get_button_one(message: types.Message):
    await message.answer("Кнопка работает!")


@dp.message_handler(Text(equals=["Кнопка №2", "Кнопка №3"]))
async def get_some_button(message: types.Message):
    await message.answer(f"Кнопка {message.text} работает!", reply_markup=ReplyKeyboardRemove())
