import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

class WeatherTool:
    """Tool to fetch weather info from OpenWeatherMap API"""

    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY", "")

    def run(self, city: str):
        if not self.api_key:
            return "Error: Missing OPENWEATHER_API_KEY in .env file"
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            r = requests.get(url, timeout=10)
            data = r.json()

            if data.get("cod") != 200:
                return f"Error: {data.get('message', 'Failed to fetch weather')}"

            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            return f"The weather in {city} is {condition} with {temp}°C."
        except Exception as e:
            return f"Error: {e}"

class WeatherAgent:
    def __init__(self):
        self.tool = WeatherTool()
        self.memory = []

    def run(self, city: str):
        # Save user query
        self.memory.append(f"USER: {city}")

        # Call tool
        result = self.tool.run(city)

        # Save response
        self.memory.append(f"AGENT: {result}")
        return result
