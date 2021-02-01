from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Test


@dp.message_handler(Command('test'))
async def enter_test(message: types.Message):
    await message.answer('2 + 2 = ?')

    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    # await state.update_data({
    #     "answer1": answer
    # })

    # async with state.proxy() as data:
    #     data["answer1"] = answer

    # await message.answer(str(answer) + "+ 6 = ?")
    await message.answer(f'{answer} + 6 = ?')

    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Молодец")
    await message.answer(f'{answer1}, {answer2}')

    await state.finish()
