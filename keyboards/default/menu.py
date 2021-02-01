from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Кнопка №1")
    ],
    [
        KeyboardButton(text="Кнопка №2"),
        KeyboardButton(text="Кнопка №3")
    ],
    ],
    resize_keyboard=True
)