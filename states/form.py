from aiogram.dispatcher.filters.state import StatesGroup, State

class Form(StatesGroup):
    Name = State()
    Email = State()
    Phone = State()
