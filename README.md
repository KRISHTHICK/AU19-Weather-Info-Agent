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
