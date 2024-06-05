from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from keyboards import reply

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    text = '''<strong>Добро пожаловать в наш магазин одежды</strong>😁!\n 
Здесь вы найдете базовые вещи высокого качества, которые подчеркнут вашу индивидуальность. 
Мы предлагаем современный дизайн и комфорт по доступным ценам💸.\n
Откройте для себя новые возможности в мире моды вместе с нами👐!'''
    await message.answer(text, reply_markup=reply.start_kb)


@user_router.message(F.text.lower() == "каталог")
@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer('Наш каталог📃', reply_markup=reply.catalog_kb)


@user_router.message(F.text.lower() == 'про нас')
@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('Про нас ')


@user_router.message(F.text.lower() == 'контакты')
@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer('Наши контакты ')


@user_router.message(F.text.lower() == 'филиалы')
@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer('Наши филиалы ')


@user_router.message(F.text.lower() == 'назад')
async def back_menu(message: types.Message):
    await message.answer('Главное меню', reply_markup=reply.start_kb)

# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == "доставка")
# @user_router.message(F.text.lower().contains('доставк'))
# @user_router.message(F.text.lower().startswith('как'))
# @user_router.message(F.text.lower().endswith('?'))
# @user_router.message(F.text.lower().startswith('как'), F.text.lower().endswith('?'))
# @user_router.message( (F.text.lower().contains('цен')) | (F.text.lower().contains('стоимост')) )
# async def echo(message: types.Message):
#    await message.answer('Сработал магический фильтр ')

