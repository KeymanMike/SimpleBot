from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from loader import dp
from utils.misc import rate_limit
from utils.db_api import User
import logging


@rate_limit(limit=10)
@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message, user: User):
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Ваши данные: {user.__dict__}')
    # Не попадает в error handler
    try:
        await message.answer("Неверное закрытие <b>тега<b>")
    except Exception as err:
        await message.answer(f"Ошибка: {err}")

    # Попадает в error handler
    # 1/0
    await message.answer("Нет такого <kek>тега</kek>")
    logging.info("Ошибка, бот не упал!")
