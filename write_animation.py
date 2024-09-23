import asyncio
from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')


async def send_letter_by_letter(client, user_id, message, delay=0.5):
    # Boshlang'ich xabarni jo'natamiz
    sent_msg = await client.send_message(user_id, "\u2060")
    sent_message = ""

    for letter in message:
        new_message = sent_message + letter  # Yangi harfni qo'shamiz

        # Agar yangi matn oldingisidan farq qilsa va bo'sh joyni e'tiborga olsa, tahrirlaymiz
        if new_message.strip() != sent_message.strip():  # strip() bo'sh joylarni olib tashlaydi
            await client.edit_message(user_id, sent_msg.id, new_message)  # Xabarni tahrirlaymiz
            sent_message = new_message  # Oxirgi matnni yangilab qo'yamiz
        await asyncio.sleep(delay)  # Harflar orasidagi kechikish

    # All messages edited
    await client.edit_message(user_id, sent_msg.id, sent_message.strip())


async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        user_id = 'user_id'  # Enter user id
        message = "men-yozyapman"  # Send message
        await send_letter_by_letter(client, user_id, message, delay=0.5)  # Harfma-harf yuborish


# Asosiy funksiyani ishga tushiramiz
asyncio.run(main())
