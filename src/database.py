import sqlite3
import os

class WeatherDatabase:
    def __init__(self, db_path=None):
        if db_path is None:
            # pega a raiz do projeto (um nível acima de src)
            base_dir = os.path.dirname(os.path.dirname(__file__))
            db_path = os.path.join(base_dir, "data", "weather.db")

        # garante que a pasta data existe
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        # conecta ao banco
        self.conn = sqlite3.connect(db_path)

        # cria tabela se não existir
        self._init_schema()

    def _init_schema(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                temperature REAL NOT NULL,
                humidity INTEGER NOT NULL,
                description TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def insert_weather(self, city, temp, humidity, description):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO weather (city, temperature, humidity, description, timestamp) VALUES (?, ?, ?, ?, datetime('now'))",
            (city, temp, humidity, description)
        )
        self.conn.commit()

    def fetch_all(self, city=None):
        cursor = self.conn.cursor()
        if city:
            cursor.execute("SELECT * FROM weather WHERE city=? ORDER BY timestamp DESC", (city,))
        else:
            cursor.execute("SELECT * FROM weather ORDER BY timestamp DESC")
        return cursor.fetchall()

    def fetch_rain_history(self, city):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM weather WHERE city=? AND description LIKE '%chuva%' ORDER BY timestamp DESC",
            (city,)
        )
        return cursor.fetchall()

    def close(self):
        self.conn.close()
