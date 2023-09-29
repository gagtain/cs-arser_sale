import asyncio

import dotenv
from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from config import init_config
from handlers import menu


async def main():
    dp = Dispatcher()
    bot = Bot("6325195132:AAEfD-9Nsg206vMeEPAoPOfM6EbRqeDUkkU", parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(menu.router)
    dotenv.load_dotenv()
    init_config()
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())