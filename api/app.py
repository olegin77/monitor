from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = 'data/botdata.db'

def execute(query, params=(), fetch=False):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(query, params)
    result = cur.fetchall() if fetch else None
    conn.commit()
    conn.close()
    return result

@app.route('/add/keyword', methods=['POST'])
def add_keyword():
    word = request.json.get('word')
    execute("INSERT OR IGNORE INTO keywords (word) VALUES (?)", (word,))
    return jsonify({"status": "ok", "word": word})

@app.route('/add/user', methods=['POST'])
def add_user():
    user_id = request.json.get('user_id')
    execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    return jsonify({"status": "ok", "user": user_id})

@app.route('/add/channel', methods=['POST'])
def add_channel():
    link = request.json.get('link')
    execute("INSERT OR IGNORE INTO channels (link) VALUES (?)", (link,))
    return jsonify({"status": "ok", "channel": link})

@app.route('/get/all', methods=['GET'])
def get_all():
    words = execute("SELECT word FROM keywords", fetch=True)
    users = execute("SELECT user_id FROM users", fetch=True)
    channels = execute("SELECT link FROM channels", fetch=True)
    return jsonify({
        "keywords": [w[0] for w in words],
        "users": [u[0] for u in users],
        "channels": [c[0] for c in channels]
    })

if __name__ == "__main__":
    app.run(port=5000)