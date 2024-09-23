import asyncio
from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')

async def send_message_with_typing(client, user_id, message):
    # Typing statusni ko'rsatamiz
    async with client.action(user_id, 'typing'):
        await asyncio.sleep(3)  # Foydalanuvchi uchun typing animatsiyasini 3 soniya davomida ko'rsatamiz
        await client.send_message(user_id, message)  # Xabar yuborish

async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        user_id = 'user_id'  # Enter user_id
        message = "Salom! Qanday yordam bera olaman?"
        await send_message_with_typing(client, user_id, message)

# Asosiy funksiyani ishga tushiramiz
asyncio.run(main())
