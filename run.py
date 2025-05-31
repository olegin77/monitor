import subprocess
import threading

def run_watcher():
    subprocess.run(["python3", "monitor/watcher.py"])

def run_bot():
    subprocess.run(["python3", "bot/main.py"])

if __name__ == "__main__":
    threading.Thread(target=run_watcher).start()
    threading.Thread(target=run_bot).start()