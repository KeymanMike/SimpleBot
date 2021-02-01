from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import allowed_users
from loader import dp


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=
                       [
                           types.InlineQueryResultArticle(
                               id="unknown",
                               title="Введите запрос!",
                               input_message_content=types.InputTextMessageContent(message_text="Введи, а не жми")
                           )
                       ],
        cache_time=5
    )

@dp.inline_handler()
async def some_q(query: types.InlineQuery):
    user = query.from_user.id
    if user not in allowed_users:
        await query.answer(
            results=[],
            switch_pm_text="Зарегайся",
            switch_pm_parameter="connect_user",
            cache_time=5
        )
        return
    else:
        await query.answer(
            results=[
                types.InlineQueryResultArticle(
                    id="1",
                    title="Титул",
                    input_message_content=types.InputTextMessageContent("Сообщение"),
                    url="https://core.telegram.org/bots/api#inlinequeryresult",
                    thumb_url="",
                    description="Описание"
                )
            ]
        )

@dp.message_handler(CommandStart(deep_link="connect_user"))
async def connect_user(message: types.Message):
    allowed_users.append(message.from_user.id)
    await message.answer("Connect",
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                             [
                                 InlineKeyboardButton(text='Войти в иноайн режим',
                                                  switch_inline_query_current_chat="Query")
                             ]
                         ])
                         )