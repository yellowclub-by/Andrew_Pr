from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def adresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Минск, ул.Богдановича 13', callback_data='adresses_1'),
        InlineKeyboardButton(text='Минск, ул. Собинова 46', callback_data='adresses_2'),
        width=1
    )
    return builder.as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(text='Сайт', url='https://www.lamoda.by/'),
        InlineKeyboardButton(text='Телеграмм', url='tg://resolve?domain=dlstudiostore')
        ]
    ]
)