# AU19-Weather-Info-Agent
Ai Agent

README.md
# 🌦️ Weather Agent

A simple end-to-end agent that fetches live weather info for a city using OpenWeatherMap API.

## Steps to Run
1. Clone this repo / copy files.
2. Install dependencies:


pip install -r requirements.txt

3. Get API key from OpenWeatherMap → put in `.env`.
4. Run:


streamlit run app.py

5. Enter a city → see weather + memory log.

🚀 How It Works

User → enters city in Streamlit

Agent → calls WeatherTool

Tool → hits OpenWeatherMap API → gets weather

Agent → saves response in memory + returns to UI

👉 This is end-to-end (UI + agent + tool + API + memory).

# 🌦️ Weather Agent (Live + Mock)
Simple Streamlit agent that fetches weather for a city. Works in **Live** mode (OpenWeatherMap) or **Mock** mode (no API needed).

## Run
1. `pip install -r requirements.txt`
2. (Optional) Add `.env` with `OPENWEATHER_API_KEY=...` for Live mode.
3. `streamlit run app.py`

## Use
- Toggle **Mock Mode** in the sidebar.
- Enter city → get weather.
- Memory log shows the conversation.

## Notes
- If no API key is found, the app auto-falls back to **Mock Mode**.
- Mock Mode is deterministic per city name.

