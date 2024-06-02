from aiogram import F, Router, types
from aiogram.types import FSInputFile

catalog_router = Router()


@catalog_router.message(F.text.lower() == 'кепка')
async def cap(message: types.Message):
    photo = FSInputFile('img\catalog\кепка.jpg')
    await message.answer_photo(photo, caption='Кепка черная,цена 45 руб.')


@catalog_router.message(F.text.lower() == 'очки')
async def sunglasses(message: types.Message):
    photo = FSInputFile('img\catalog\очки.jpg')
    await message.answer_photo(photo, caption='Очки черные, цена 45 руб.')


@catalog_router.message(F.text.lower() == 'куртка')
async def jacket(message: types.Message):
    photo = FSInputFile('img\catalog\куртка.jpg')
    await message.answer_photo(photo, caption='Куртка черная, цена 150 руб.')


@catalog_router.message(F.text.lower() == 'свитшот')
async def sweatshirt(message: types.Message):
    photo = FSInputFile('img\catalog\свитшот.jpg')
    await message.answer_photo(photo, caption='Свитшот черный, цена 80 руб.')


@catalog_router.message(F.text.lower() == 'футболка')
async def t_shirt(message: types.Message):
    photo = FSInputFile('img\catalog\футболка.jpg')
    await message.answer_photo(photo, caption='Футболка черная, цена 40 руб.')


@catalog_router.message(F.text.lower() == 'джинсы')
async def jeans(message: types.Message):
    photo = FSInputFile('img\catalog\джинсы.jpg')
    await message.answer_photo(photo, caption='Джинсы черные, цена 120 руб.')
