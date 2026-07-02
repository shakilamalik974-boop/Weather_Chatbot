import streamlit as st
from weather_api import get_current_weather
from llm import chat_with_llm

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


user_input = st.chat_input("Ask anything about weather...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    text = user_input.lower()

    # simple city extraction (lightweight, no LLM dependency)
    city = None
    words = user_input.split()

    for w in words:
        if w.istitle():
            city = w

    if city:
        st.session_state.last_city = city
    else:
        city = st.session_state.last_city

    weather_data = None

    if city:
        response = get_current_weather(city)
        if response.status_code == 200:
            weather_data = response.json()

    reply = chat_with_llm(
        user_query=user_input,
        weather_data=weather_data,
        chat_history=st.session_state.messages
    )

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)