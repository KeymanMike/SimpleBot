from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text='➽', request_location=True)
        ]
    ],
    resize_keyboard=True
)