import threading
import subprocess
from flask import Flask, render_template
from src.database import WeatherDatabase

app = Flask(__name__)

@app.route("/")
def index():
    db = WeatherDatabase()
    data = db.fetch_all()
    db.close()
    return render_template("index.html", weather=data)

def run_main():
    """Executa o main.py em paralelo"""
    subprocess.run(["python", "src/main.py"])

if __name__ == "__main__":
    # roda o main.py em uma thread separada
    t = threading.Thread(target=run_main, daemon=True)
    t.start()

    # inicia o servidor Flask
    app.run(debug=True)
