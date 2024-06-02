import asyncio
from aiogram import Bot, Dispatcher

TOKEN = "7127422770:AAGqCQ1JjxdF4Td36Oj1WyDodUoE7UfmrIE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

from handlers.user_privat import user_router
from handlers.catalog import catalog_router
from handlers.user_group import group_router

dp.include_router(user_router)
dp.include_router(catalog_router)
dp.include_router(group_router)


async def main():
    print("Бот запущен")
    await  dp.start_polling(bot)


asyncio.run(main())
