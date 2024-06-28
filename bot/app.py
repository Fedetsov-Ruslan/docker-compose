import asyncio

import os
import aiohttp

from datetime import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types


load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()


async def on_startup():
    await bot.delete_webhook()
    dp.http_session = aiohttp.ClientSession()

async def on_shutdown():
    await dp.http_session.close()
    await bot.session.close()


async def process_message_from_user(message_text: str, chat_id: int):
    user_id = '' # беретя из базы данных, тот кому хотим отправить сообщение
    await bot.send_message(chat_id=user_id, text=message_text)
            

async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await dp.storage.close()

if __name__ == '__main__':
    asyncio.run(main())