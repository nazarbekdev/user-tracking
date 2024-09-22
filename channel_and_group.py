from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')

client = TelegramClient('anon', api_id, api_hash)


async def main():
    # Enter your_channel or your_group link
    group = 'your_link'

    # Get all users
    participants = await client.get_participants(group)

    # print users
    for participant in participants:
        print(f'Ism: {participant.first_name}, Username: {participant.username}, ID: {participant.id}')


# Working function
with client:
    client.loop.run_until_complete(main())
