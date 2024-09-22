import os
from telethon import TelegramClient, events
from dotenv import load_dotenv
load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
bot_token = os.getenv('bot_token')

client = TelegramClient('bot', api_id, api_hash)


@client.on(events.NewMessage)
async def handler(event):
    await event.reply('Salom! Men botman.')

client.start(bot_token=bot_token)
client.run_until_disconnected()
