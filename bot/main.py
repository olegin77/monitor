from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import json, os

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN", "YOUR_BOT_TOKEN")

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['add_word'])
async def add_word(message: types.Message):
    word = message.get_args()
    with open('data/config.json', 'r+') as f:
        config = json.load(f)
        if word and word not in config['keywords']:
            config['keywords'].append(word)
            f.seek(0)
            json.dump(config, f, indent=4)
            f.truncate()
            await message.reply(f"Ключевое слово '{word}' добавлено.")
        else:
            await message.reply("Слово уже есть или не указано.")

@dp.message_handler(commands=['add_user'])
async def add_user(message: types.Message):
    try:
        user_id = int(message.get_args())
        with open('data/config.json', 'r+') as f:
            config = json.load(f)
            if user_id not in config['users']:
                config['users'].append(user_id)
                f.seek(0)
                json.dump(config, f, indent=4)
                f.truncate()
                await message.reply(f"Пользователь {user_id} добавлен.")
            else:
                await message.reply("Пользователь уже есть.")
    except:
        await message.reply("Неверный формат ID.")

@dp.message_handler(commands=['add_channel'])
async def add_channel(message: types.Message):
    channel = message.get_args()
    with open('data/config.json', 'r+') as f:
        config = json.load(f)
        if channel and channel not in config['channels']:
            config['channels'].append(channel)
            f.seek(0)
            json.dump(config, f, indent=4)
            f.truncate()
            await message.reply(f"Канал {channel} добавлен.")
        else:
            await message.reply("Канал уже есть или не указан.")

def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()