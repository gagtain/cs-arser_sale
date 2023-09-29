import asyncio

import dotenv
from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from config import init_config, Config
from handlers import menu, weapons


async def main():
    dotenv.load_dotenv()
    init_config()
    dp = Dispatcher()
    bot = Bot(Config.telegram_token, parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(menu.router, weapons.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
