import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "7127422770:AAGqCQ1JjxdF4Td36Oj1WyDodUoE7UfmrIE"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет, это бот clothes_shop_MInsk')


@dp.message()
async def echo(message: types.Message):
    await message.answer('бот пока находится в разработке')
    user_text = message.text
    await message.answer(user_text)


async def main():
    await  dp.start_polling(bot)


asyncio.run(main())
