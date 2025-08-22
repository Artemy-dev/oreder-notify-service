from dotenv import load_dotenv
import os
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from faststream.rabbit import RabbitBroker

load_dotenv()
token = os.getenv("TOKEN")
bot = Bot(token=token)
dp = Dispatcher()
broker = RabbitBroker()

@broker.subscriber("orders")
async def handle_orders(data: str):
    await bot.send_message(
        chat_id=os.getenv("CHAT_ID"),
        text=data,
    )

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"ID: {message.chat.id}")

async def main() -> None:
    async with broker:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        await broker.start()
        logging.info("Broker started")
        await dp.start_polling(bot)
    logging.info("Broker stopped")

if __name__ == "__main__":
    asyncio.run(main())