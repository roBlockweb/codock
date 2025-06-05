import sqlite3
from .config import Config

class DBManager:
    def __init__(self, path=None):
        self.path = path or Config.DB_PATH
        self._init_db()

    def _init_db(self):
        self.conn = sqlite3.connect(self.path)
        cur = self.conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS history(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        agent TEXT,
                        message TEXT
                      )''')
        self.conn.commit()

    def save_message(self, agent, message):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO history(agent, message) VALUES (?, ?)', (agent, message))
        self.conn.commit()

    def fetch_messages(self, limit=100):
        cur = self.conn.cursor()
        cur.execute('SELECT agent, message FROM history ORDER BY id DESC LIMIT ?', (limit,))
        return cur.fetchall()
