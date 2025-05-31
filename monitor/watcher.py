from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import json, asyncio, time, os

api_id = int(os.getenv("TELETHON_API_ID", "YOUR_API_ID"))
api_hash = os.getenv("TELETHON_API_HASH", "YOUR_API_HASH")
session_name = 'monitor/session/user'

with open('data/config.json') as f:
    config = json.load(f)

keywords = config['keywords']
channels = config['channels']
users = config['users']

client = TelegramClient(session_name, api_id, api_hash)

async def check_channels():
    async with client:
        for link in channels:
            entity = await client.get_entity(link)
            async for message in client.iter_messages(entity, limit=10):
                if any(word.lower() in message.text.lower() for word in keywords if message.text):
                    for user_id in users:
                        await client.send_message(user_id, f"<b>[{link}]</b>\n{message.text[:300]}")

if __name__ == "__main__":
    while True:
        asyncio.run(check_channels())
        time.sleep(60)