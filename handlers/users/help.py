from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit
from filters import IsPrivate


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp(), IsPrivate())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/test - Пройти тест',
        '/form - Ввод данных',
        '/menu - Глянь и узнаешь'
    ]
    await message.answer('\n'.join(text))
