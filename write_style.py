import asyncio
from telethon import TelegramClient, events
from telethon.tl.custom import Button
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')


# Funksiya xabar yuborish uchun
async def send_interactive_message(client, user_id):
    await client.send_message(
        user_id,
        'Qaysi variantni tanlaysiz?',
        buttons=[
            [Button.inline('Variant 1', b'1'), Button.inline('Variant 2', b'2')],
        ]
    )


# Tanlov natijasini ishlovchi funksiya
@events.register(events.NewMessage(pattern='Assalomu alaykum'))
async def handle_choice_1(event):
    await event.respond('Va alaykum assalom')


@events.register(events.NewMessage(pattern='Yaxshimisiz'))
async def handle_choice_2(event):
    await event.respond('Yaxshi rahmat')


async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        user_id = 'user_id'  # Enter user_id
        await send_interactive_message(client, user_id)

        # Tanlovni ishlovchi event handlerlarni qo'shamiz
        client.add_event_handler(handle_choice_1)
        client.add_event_handler(handle_choice_2)

        print("Bot ishlayapti...")
        await client.run_until_disconnected()


# Asosiy funksiyani ishga tushiramiz
asyncio.run(main())
