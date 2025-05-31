import os
from dotenv import load_dotenv
load_dotenv()

from telethon.sync import TelegramClient
import sqlite3, asyncio, time

api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
session_name = 'monitor/session/user'

def get_data():
    conn = sqlite3.connect('data/botdata.db')
    c = conn.cursor()
    c.execute("SELECT word FROM keywords")
    keywords = [row[0] for row in c.fetchall()]
    c.execute("SELECT link FROM channels")
    channels = [row[0] for row in c.fetchall()]
    c.execute("SELECT user_id FROM users")
    users = [row[0] for row in c.fetchall()]
    conn.close()
    return keywords, channels, users

client = TelegramClient(session_name, api_id, api_hash)

async def check_channels():
    keywords, channels, users = get_data()
    async with client:
        for link in channels:
            try:
                entity = await client.get_entity(link)
                async for message in client.iter_messages(entity, limit=10):
                    if message.text and any(word.lower() in message.text.lower() for word in keywords):
                        for user_id in users:
                            await client.send_message(user_id, f"<b>[{link}]</b>\n{message.text[:300]}")
            except Exception as e:
                print(f"Ошибка при обработке {link}: {e}")

if __name__ == "__main__":
    while True:
        asyncio.run(check_channels())
        time.sleep(60)