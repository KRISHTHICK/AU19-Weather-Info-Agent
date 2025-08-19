import streamlit as st
from agent import WeatherAgent

st.set_page_config(page_title="Weather Agent", page_icon="🌦️", layout="centered")

st.title("🌦️ Simple Weather Agent")
st.write("Type a city name and get live weather info.")

# Initialize agent
if "agent" not in st.session_state:
    st.session_state.agent = WeatherAgent()

city = st.text_input("Enter city name:", "")

if st.button("Get Weather"):
    if not city.strip():
        st.warning("Please enter a city.")
    else:
        response = st.session_state.agent.run(city)
        st.success(f"🤖 {response}")

st.divider()
st.subheader("🧾 Conversation Memory")
for msg in st.session_state.agent.memory:
    st.write(msg)
