import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from config import TOKEN

from handlers import rtr

async def main():
	bot = Bot(token=TOKEN)
	dp = Dispatcher()
	dp.include_router(rtr)
	await dp.start_polling(bot)

if __name__ == '__main__':
	
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print("Bot stopped")