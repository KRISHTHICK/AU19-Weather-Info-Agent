import os
import math
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()  # loads OPENWEATHER_API_KEY from .env if present

class WeatherTool:
    """Live weather via OpenWeatherMap API (metric units)."""
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY", "")

    def has_key(self) -> bool:
        return bool(self.api_key)

    def run(self, city: str) -> str:
        if not self.api_key:
            return "Error: Missing OPENWEATHER_API_KEY."
        try:
            url = (
                "http://api.openweathermap.org/data/2.5/weather"
                f"?q={city}&appid={self.api_key}&units=metric"
            )
            r = requests.get(url, timeout=10)
            data = r.json()

            if data.get("cod") != 200:
                return f"Error: {data.get('message', 'Failed to fetch weather')}"

            temp = data["main"]["temp"]
            feels = data["main"].get("feels_like")
            hum = data["main"].get("humidity")
            cond = data["weather"][0]["description"]
            wind = data.get("wind", {}).get("speed")
            parts = [
                f"Weather in {city}: {cond}",
                f"Temp: {temp}°C",
            ]
            if feels is not None:
                parts.append(f"Feels like: {feels}°C")
            if hum is not None:
                parts.append(f"Humidity: {hum}%")
            if wind is not None:
                parts.append(f"Wind: {wind} m/s")
            return " | ".join(parts)
        except Exception as e:
            return f"Error: {e}"

class MockWeatherTool:
    """
    Deterministic mock weather generator:
    - Creates a pseudo-random but repeatable temp/humidity/wind from city name.
    - Useful for offline demos and tests.
    """
    def _seed_from_city(self, city: str) -> int:
        h = hashlib.sha256(city.strip().lower().encode("utf-8")).hexdigest()
        return int(h[:8], 16)

    def run(self, city: str) -> str:
        seed = self._seed_from_city(city)
        # pseudo values
        temp = round(((seed % 350) / 10.0) - 5.0, 1)          # -5.0°C to 30.0°C
        feels = round(temp + ((seed >> 4) % 6 - 3) * 0.7, 1)  # ±2°C-ish
        hum = 30 + (seed % 71)                                # 30%..100%
        wind = round(((seed >> 8) % 150) / 10.0, 1)           # 0.0..15.0 m/s
        conds = ["clear sky", "few clouds", "scattered clouds", "broken clouds",
                 "light rain", "moderate rain", "thunderstorm", "mist"]
        cond = conds[(seed >> 12) % len(conds)]
        return f"[MOCK] Weather in {city}: {cond} | Temp: {temp}°C | Feels like: {feels}°C | Humidity: {hum}% | Wind: {wind} m/s"

class WeatherAgent:
    def __init__(self):
        self.live_tool = WeatherTool()
        self.mock_tool = MockWeatherTool()
        self.use_mock = not self.live_tool.has_key()  # default to mock if no key
        self.memory = []

    def has_api_key(self) -> bool:
        return self.live_tool.has_key()

    def set_mode(self, use_mock: bool):
        self.use_mock = use_mock or not self.has_api_key()

    def run(self, city: str) -> str:
        self.memory.append(f"USER: {city}")
        tool = self.mock_tool if self.use_mock else self.live_tool
        result = tool.run(city)
        self.memory.append(f"AGENT: {result}")
        return result

    def clear_memory(self):
        self.memory.clear()
