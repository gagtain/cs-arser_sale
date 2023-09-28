import asyncio

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from handlers import menu


async def main():
    dp = Dispatcher()
    bot = Bot("6325195132:AAEfD-9Nsg206vMeEPAoPOfM6EbRqeDUkkU", parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(menu.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())