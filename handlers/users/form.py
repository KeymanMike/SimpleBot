from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Form

@dp.message_handler(Command('form'))
async def enter_test(message: types.Message):
    await message.answer('Введите ваше Имя:')

    await Form.Name.set()


@dp.message_handler(state=Form.Name)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data({
        "name": answer
    })

    await message.answer(f'Введите ваш E-mail:')

    await Form.Email.set()


@dp.message_handler(state=Form.Email)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data({
        "email": answer
    })

    await message.answer(f'Введите ваш номер телефона:')

    await Form.Phone.set()


@dp.message_handler(state=Form.Phone)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data({
        "phone": answer
    })
    user_data = await state.get_data()
    await message.answer(f'Привет! Ты ввел следующие данные:\n'
                         f'Имя - {user_data["name"]}\n'
                         f'Email - {user_data["email"]}\n'
                         f'Телефон - {user_data["phone"]}')

    await state.finish()