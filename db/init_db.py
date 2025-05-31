import sqlite3

def init_db():
    conn = sqlite3.connect('data/botdata.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS keywords (id INTEGER PRIMARY KEY AUTOINCREMENT, word TEXT UNIQUE NOT NULL)")
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE NOT NULL)")
    c.execute("CREATE TABLE IF NOT EXISTS channels (id INTEGER PRIMARY KEY AUTOINCREMENT, link TEXT UNIQUE NOT NULL)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()