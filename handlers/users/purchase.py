import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_button import choice, elephant_keyboard
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(text="Инлайн кнопки", reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="elephant"))
async def buyinf_elephant(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Слонов {quantity}",
                              reply_markup=elephant_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("ОТМЕНА", show_alert=True)
    await call.message.edit_reply_markup()

    # await bot.edit_message_reply_markup(chat_id=call.from_user.id,
    #                                     message_id= call.message.message_id,
    #                                     reply_markup=None)
