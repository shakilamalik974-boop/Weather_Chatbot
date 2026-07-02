import streamlit as st
from weather_api import get_current_weather
from llm import chat_with_llm
import re

# Page setup
st.set_page_config(page_title="AI Weather Chatbot", page_icon="🌦️")

# Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_city" not in st.session_state:
    st.session_state.last_city = ""

st.title("🌦️ AI Weather Chatbot")

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# ---------- CITY EXTRACTION (FIXED) ----------
def extract_city(text):
    invalid_words = [
        "tell", "only", "just", "what", "how", "please",
        "weather", "temperature", "humidity", "forecast"
    ]

    words = re.findall(r"[A-Za-z]+", text)

    for w in words:
        if w.lower() not in invalid_words and w[0].isupper():
            return w

    return None


# ---------- INPUT ----------
user_input = st.chat_input("Ask anything about weather...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # extract city safely
    city = extract_city(user_input)

    # fallback to memory
    if not city:
        city = st.session_state.last_city
    else:
        st.session_state.last_city = city

    weather_data = None

    # fetch weather only if city exists
    if city:
        response = get_current_weather(city)

        if response.status_code == 200:
            weather_data = response.json()

    # generate response from LLM
    reply = chat_with_llm(
        user_query=user_input,
        weather_data=weather_data,
        chat_history=st.session_state.messages
    )

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)