import asyncio
from aiogram import Bot, Dispatcher


TOKEN = "7127422770:AAGqCQ1JjxdF4Td36Oj1WyDodUoE7UfmrIE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

from handlers.user_privat import user_router
dp.include_router(user_router)

from handlers.user_group import group_router
dp.include_router(group_router)

async def main():
    await  dp.start_polling(bot)


asyncio.run(main())
