import asyncio
from aiogram import Bot, Dispatcher

from helpers.hendlers import router

from Datbase.things import db_main



async def main():
    await db_main()
    bot = Bot(token="6904015579:AAHKEbRngR1R0ID8Kv1wD78kYPBT09gQE7w")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
