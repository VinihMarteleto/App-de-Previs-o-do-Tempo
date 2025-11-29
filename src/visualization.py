import matplotlib.pyplot as plt

from database import WeatherDatabase


def plot_weather(city):
    db = WeatherDatabase()
    data = db.fetch_all(city)
    db.close()

    if not data:
        print("Nenhum dado encontrado para essa cidade.")
        return

    timestamps = [row[5] for row in data]
    temps = [row[2] for row in data]
    hums = [row[3] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temps, label="Temperatura (°C)", color="red")
    plt.plot(timestamps, hums, label="Umidade (%)", color="blue")
    plt.xlabel("Data")
    plt.ylabel("Valores")
    plt.title(f"Histórico de Clima - {city}")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()