from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def adresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Пункт выдачи 1', callback_data='adresses_1'),
        InlineKeyboardButton(text='Пункт выдачи 2', callback_data='adresses_2'),
        InlineKeyboardButton(text='Пункт выдачи 3', callback_data='adresses_3'),
        width=1
    )
    return builder.as_markup()