from aiogram.filters import CommandStart, Command
from aiogram import types, Router

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет, это бот clothes_shop_MInsk')


@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer('Наш каталог ')


@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('Про нас ')


@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer('Наши контакты ')


@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer('Наши филиалы ')


@user_router.message()
async def echo(message: types.Message):
    await message.answer('бот пока находится в разработке')
    user_text = message.text
    await message.answer(user_text)
