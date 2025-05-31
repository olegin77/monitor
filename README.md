# Telegram Monitor Bot with .env and Absolute Session Path

## 📌 Описание

Бот сканирует публичные Telegram-каналы с помощью Telethon UserBot и находит сообщения, содержащие заданные ключевые слова. Найденные сообщения пересылаются в Telegram-профили пользователей, указанных в базе данных. Все параметры конфигурации берутся из `.env`.

---

## 📁 Структура проекта

- `bot/` — Telegram-бот на Aiogram
- `monitor/` — Telethon UserBot для сканирования каналов
- `monitor/session/` — папка для сессии пользователя Telethon
- `api/` — Flask REST API для управления данными
- `db/` — скрипт инициализации SQLite базы
- `data/` — содержит `botdata.db`
- `.env` — переменные окружения (API ID, HASH, BOT TOKEN)
- `run.py` — параллельный запуск бота и сканера
- `requirements.txt` — список зависимостей

---

## ⚙️ Настройка `.env`

Создай файл `.env` в корне проекта:

```env
TELEGRAM_API_ID=ваш_api_id
TELEGRAM_API_HASH=ваш_api_hash
TELEGRAM_API_TOKEN=токен_бота_от_BotFather
```

---

## 🚀 Установка на VPS (Ubuntu)

1. Установи Python и pip:

```bash
sudo apt update && sudo apt install python3-pip -y
```

2. Установи зависимости:

```bash
pip3 install -r requirements.txt
```

3. Создай `.env` файл:

```bash
nano .env
# вставь TELEGRAM_API_ID, TELEGRAM_API_HASH и TELEGRAM_API_TOKEN
```

4. Инициализируй базу данных:

```bash
python3 db/init_db.py
```

5. Запусти Flask API:

```bash
python3 api/app.py
```

6. Добавь ключевые слова, каналы и пользователей через CURL или Postman:

```bash
curl -X POST http://localhost:5000/add/keyword -H "Content-Type: application/json" -d '{"word":"вакансия"}'
curl -X POST http://localhost:5000/add/channel -H "Content-Type: application/json" -d '{"link":"https://t.me/examplechannel"}'
curl -X POST http://localhost:5000/add/user -H "Content-Type: application/json" -d '{"user_id":123456789}'
```

7. Первый запуск `watcher.py` — пройти авторизацию:

```bash
python3 monitor/watcher.py
# Введите номер, Telegram пришлёт код
```

8. Запусти всё вместе:

```bash
python3 run.py
```

---

## 🌐 REST API Эндпоинты

| Метод | URL                | JSON-параметры                   |
|-------|--------------------|----------------------------------|
| POST  | `/add/keyword`     | `{ "word": "вакансия" }`         |
| POST  | `/add/channel`     | `{ "link": "https://..." }`      |
| POST  | `/add/user`        | `{ "user_id": 123456789 }`       |
| GET   | `/get/all`         | —                                |

---

## 💡 Особенности

- Используется **абсолютный путь** к `user.session` → меньше ошибок на VPS
- Все настройки загружаются через `.env`
- Хранение данных — SQLite

---

## 🛡 Безопасность

- Не публикуй `.env` и `.session` файлы
- При потере контроля над session-файлом — удали `user.session` и авторизуйся заново

---

## 📦 Автоматизация (по желанию)

Добавим запуск через `systemd`, `supervisor`, Docker-контейнер или HTTPS через nginx по твоему запросу.