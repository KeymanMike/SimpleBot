from aiogram import types
from loader import dp
from filters import IsPrivate


@dp.message_handler(IsPrivate())
async def bot_echo(message: types.Message):

    text = message.text

    await message.answer(text)

