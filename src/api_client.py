import os

import requests
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

class WeatherAPIClient:
    """
    Cliente para interagir com a API do OpenWeatherMap.
    Responsável por buscar dados de clima para uma cidade específica.
    """

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("API Key não encontrada. Configure a variável OPENWEATHER_API_KEY no arquivo .env.")

    def get_weather_data(self, city: str) -> dict:
        """
        Busca dados de clima para uma cidade.

        Args:
            city (str): Nome da cidade (ex: "São Paulo,BR").

        Returns:
            dict: Dados de clima (temperatura em Celsius, umidade, descrição).

        Raises:
            requests.exceptions.RequestException: Se houver erro na requisição.
        """
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",  # Temperatura em Celsius
            "lang": "pt_br"     # Descrição em português
        }

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()  # Levanta erro se status não for 200

        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }