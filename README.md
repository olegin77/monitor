# Telegram Monitor Bot

## 📌 Описание

Этот бот мониторит Telegram-каналы, ищет по заданным ключевым словам, и отправляет найденные сообщения выбранным пользователям в Telegram. Управление происходит через Telegram-бота или REST API.

---

## 📁 Структура

- `bot/` — Telegram-бот (Aiogram)
- `monitor/` — мониторинг каналов (Telethon UserBot)
- `api/` — Flask REST API для управления
- `db/` — инициализация базы данных SQLite
- `data/` — содержит `botdata.db`
- `run.py` — запускает Telegram-бота и мониторинг
- `requirements.txt` — зависимости проекта

---

## 🚀 Установка на VPS (Ubuntu)

1. **Установи Python 3 и pip:**

```bash
sudo apt update && sudo apt install python3-pip -y
```

2. **Клонируй или загрузи проект:**

```bash
unzip final_telegram_monitor_bot_vps_ready.zip
cd telegram_monitor_bot
```

3. **Установи зависимости:**

```bash
pip3 install -r requirements.txt
```

4. **Создай файл `.env` (необязательно, можно через переменные окружения):**

```env
TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash
TELEGRAM_API_TOKEN=your_telegram_bot_token
```

5. **Инициализируй базу данных:**

```bash
python3 db/init_db.py
```

6. **Запусти Flask API (для добавления слов/каналов/пользователей):**

```bash
python3 api/app.py
```

7. **Запусти мониторинг и Telegram-бота:**

```bash
python3 run.py
```

---

## 📡 API Эндпоинты

| Метод | URL                | Тело запроса (JSON)           |
|-------|--------------------|-------------------------------|
| POST  | `/add/keyword`     | `{ "word": "вакансия" }`      |
| POST  | `/add/user`        | `{ "user_id": 123456789 }`    |
| POST  | `/add/channel`     | `{ "link": "https://t.me/..."}` |
| GET   | `/get/all`         | —                             |

---

## 📬 Пример добавления через curl

```bash
curl -X POST http://localhost:5000/add/keyword -H "Content-Type: application/json" -d '{"word":"вакансия"}'
```

---

## 🔐 Примечание

- `monitor/watcher.py` использует Telethon UserBot: при первом запуске потребуется ввести номер телефона и код.
- Бот может читать только публичные каналы или те, где вы — админ.

---

## ✅ Готово!

Запустите `run.py`, и система будет автоматически мониторить каналы и присылать уведомления по ключевым словам.