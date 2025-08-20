import streamlit as st
from agent import WeatherAgent

st.set_page_config(page_title="Weather Agent", page_icon="🌦️", layout="centered")

st.title("🌦️ Weather Agent (Live + Mock)")
st.write("Enter a city to get weather. Toggle Mock Mode to run without API.")

# Init agent in session
if "agent" not in st.session_state:
    st.session_state.agent = WeatherAgent()

# Sidebar controls
st.sidebar.header("⚙️ Settings")
use_mock = st.sidebar.checkbox("Mock Mode (no API key required)", value=st.session_state.agent.use_mock)
st.session_state.agent.set_mode(use_mock)

st.sidebar.write("Mode:", "**Mock**" if st.session_state.agent.use_mock else "**Live (OpenWeatherMap)**")
if not st.session_state.agent.use_mock and not st.session_state.agent.has_api_key():
    st.sidebar.warning("No OPENWEATHER_API_KEY found. Auto-switching to Mock Mode.")
    st.session_state.agent.set_mode(True)

# Main UI
city = st.text_input("City name", placeholder="e.g., Mumbai")

col1, col2 = st.columns([1,1])
if col1.button("Get Weather"):
    if not city.strip():
        st.warning("Please enter a city.")
    else:
        result = st.session_state.agent.run(city.strip())
        st.success(f"🤖 {result}")

if col2.button("Clear Memory"):
    st.session_state.agent.clear_memory()
    st.info("Memory cleared.")

st.divider()
st.subheader("🧾 Conversation Memory")
for msg in st.session_state.agent.memory:
    st.write(msg)
