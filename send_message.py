import asyncio
import os
import lorem
from dotenv import load_dotenv
from telethon import TelegramClient
import random
load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')

svg = os.getenv('svg')
svg_lst = svg.split(',')
users = os.getenv('users')
users_lst = users.split(',')


async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        for i in range(15):
            # await client.send_message(int(random.choice(users_lst)), random.choice(svg_lst))
            await client.send_message(int(random.choice(users_lst)), lorem.sentence())

# Working function
asyncio.run(main())
