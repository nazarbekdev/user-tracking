from telethon.sync import TelegramClient
from telethon.tl.types import UserStatusOnline, UserStatusOffline
from dotenv import load_dotenv
load_dotenv()
import time, os

# Siz olgan API_ID va API_HASH ni kiriting
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')

# Kirishni boshlaymiz
client = TelegramClient('session_name', api_id, api_hash)

# Kirish
client.start()

# Foydalanuvchi ID yoki username ni kiriting
user_id = 'uz_pydev'


# Foydalanuvchi holatini kuzatish uchun funksiya
def check_status():
    user = client.get_entity(user_id)
    status = user.status

    if isinstance(status, UserStatusOnline):
        print(f"{user.username} hozir onlayn.")
    elif isinstance(status, UserStatusOffline):
        print(f"{user.username} oflayn bo'lgan vaqti: {status.was_online}")
    else:
        print(f"{user.username} hozir noma'lum holatda.")

    return status


# Har 5 soniyada foydalanuvchi holatini tekshirish
while True:
    status = check_status()
    time.sleep(5)

client.run_until_disconnected()
