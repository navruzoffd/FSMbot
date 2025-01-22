from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
)

def start_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Создать чат"), KeyboardButton(text="Добавить сообщение")]
    ], resize_keyboard=True)
    return keyboard