from src.api_client import WeatherAPIClient
from src.database import WeatherDatabase
from src.visualization import plot_weather

def menu():
    print("\n=== previsão do tempo ===")
    print("1. Consultar clima de uma cidade")
    print("2. Visualizar dados históricos")
    print("3. Gerar gráfico")
    print("0. Sair")


def main():
    client = WeatherAPIClient()
    db = WeatherDatabase()

    while True:
        menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            city = input("Digite o nome da cidade (ex: São Paulo,BR): ")
            try:
                data = client.get_weather_data(city)
                db.insert_weather(
                    data["city"],
                    data["temperature"],
                    data["humidity"],
                    data["description"]
                )
                print(
                    f"\nClima em {data['city']}: "
                    f"{data['temperature']}°C, {data['humidity']}% - {data['description']}"
                )
            except Exception as e:
                print(f"Erro ao consultar clima: {e}")

        elif choice == "2":
            city = input("Digite o nome da cidade para visualizar histórico: ")
            try:
                records = db.fetch_all(city)
                if records:
                    for r in records:
                        # r[0]=id, r[1]=city, r[2]=temp, r[3]=humidity, r[4]=desc, r[5]=timestamp
                        print(f"{r[5]} - {r[1]}: {r[2]}°C, {r[3]}% - {r[4]}")
                else:
                    print("Nenhum registro encontrado para essa cidade.")
            except Exception as e:
                print(f"Erro ao buscar histórico: {e}")

        elif choice == "3":
            city = input("Digite o nome da cidade para gerar gráfico: ")
            try:
                plot_weather(city)
            except Exception as e:
                print(f"Erro ao gerar gráfico: {e}")

        elif choice == "0":
            db.close()
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()