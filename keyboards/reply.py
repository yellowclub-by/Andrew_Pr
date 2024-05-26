from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Каталог'),
            KeyboardButton(text='Про нас'),
        ],

        [
            KeyboardButton(text='Контакты'),
            KeyboardButton(text='Филиалы')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что хотите?'
)

catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Кепка'),
            KeyboardButton(text='Очки')
        ],
        [
            KeyboardButton(text='Куртка'),
            KeyboardButton(text='Свитшот')
        ],
        [
            KeyboardButton(text='Футболка'),
            KeyboardButton(text='Джинсы')

        ]
    ],
    resize_keyboard=True
)
