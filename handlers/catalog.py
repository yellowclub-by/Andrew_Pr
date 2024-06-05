from aiogram import F, Router, types
from aiogram.types import FSInputFile

catalog_router = Router()


@catalog_router.message(F.text.lower() == 'кепка')
async def cap(message: types.Message):
    photo = FSInputFile('img\catalog\кепка.jpg')
    text = '''Эта черная рваная кепка — идеальное дополнение к вашему стильному образу.\n
Изготовлена из качественных материалов, она обеспечит комфорт и долговечность. 
Идеально подходит для повседневного ношения и создания модных образов.\n
Цена: 45 BYN'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'очки')
async def sunglasses(message: types.Message):
    photo = FSInputFile('img\catalog\очки.jpg')
    text = '''Эти черные модные очки станут ярким акцентом в вашем гардеробе.\n
Очки обеспечивают надежную защиту от солнца благодаря высококачественным линзам.
Добавьте элегантности и утонченности вашему образу с этими стильными аксессуарами.\n
Цена: 50 BYN'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'куртка')
async def jacket(message: types.Message):
    photo = FSInputFile('img\catalog\куртка.jpg')
    text = '''Эта черная куртка сочетает в себе стиль и функциональность.\n
Куртка отлично подходит для повседневного ношения и легко комбинируется с любым образом.
Сделайте свой гардероб более универсальным с этой модной и практичной курткой.\n
Цена: 150 BYN'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'свитшот')
async def sweatshirt(message: types.Message):
    photo = FSInputFile('img\catalog\свитшот.jpg')
    text = '''Этот черный свитшот станет незаменимой частью вашего гардероба.\n
Стильный дизайн и удобный крой делают его идеальным выбором для повседневного образа.
Доверьтесь комфорту и модному виду с этим элегантным свитшотом.\n
Цена: 100 BYN'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'футболка')
async def t_shirt(message: types.Message):
    photo = FSInputFile('img\catalog\футболка.jpg')
    text = '''Эта черная футболка - это классика стиля и удобства.\n
Ее универсальный дизайн позволяет легко комбинировать с различными нижней одеждой, подходящей к любому образу.
Добавьте эту модную футболку в свой гардероб для стильных и комфортных повседневных нарядов.\n
Цена: 50 BYN'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'джинсы')
async def jeans(message: types.Message):
    photo = FSInputFile('img\catalog\джинсы.jpg')
    text = '''Эти джинсы - надежный выбор для стильного повседневного образа.\n
Их дизайн и комфортный крой подходят для любой ситуации.
Обновите свой гардероб с этими универсальными и модными джинсами.\n
Цена: 130 BYN'''
    await message.answer_photo(photo, caption=text)
