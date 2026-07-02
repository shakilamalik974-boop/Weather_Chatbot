import streamlit as st

from weather_api import get_current_weather, get_forecast
from llm import extract_intent, generate_response



# Page Setup
st.set_page_config(
    page_title="AI Weather Chatbot",
    page_icon="🌦️"
)



# Session Memory

if "messages" not in st.session_state:
    st.session_state.messages = []


if "last_city" not in st.session_state:
    st.session_state.last_city = ""



# UI Styling

st.markdown("""
<style>

.main {
    background-color: #f5f9ff;
}

h1 {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)



# Title

st.title("🌦️ AI Weather Chatbot")

st.caption(
    "Ask anything about weather"
)



# Chat History

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])





# User Input

user_input = st.chat_input(
    "Ask about weather..."
)



if user_input:


    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )


    with st.chat_message("user"):
        st.write(user_input)



    # Understand user query using LLM

    analysis = extract_intent(user_input)



    intent = analysis["intent"]

    city = analysis["city"]
    st.write("Analysis:", analysis)
    st.write("Intent:", intent)
    st.write("City:", city)



    # Save city memory

    if city:

        st.session_state.last_city = city


    else:

        city = st.session_state.last_city




    # Non Weather Query

    if intent == "not_weather":


        bot_response = """
I am a Weather Assistant 🌦️

I can help you with:
• Current weather
• Temperature
• Forecast
• Weather recommendations

Please ask me something related to weather.
"""


    # Current Weather

    elif intent == "current_weather":


        if city == "":

            bot_response = "Please mention a city name."


        else:


            response = get_current_weather(city)
            
            st.write(response.status_code)
            st.json(response.json())



            if response.status_code == 200:


                data = response.json()



                bot_response = generate_response(
                    user_query=user_input,
                    weather_data=data
                )


            else:

                bot_response = "I couldn't find this city. Please try another city."





    # Forecast

    elif intent == "forecast":


        if city == "":

            bot_response = "Please mention a city name."


        else:


            response = get_forecast(city)



            if response.status_code == 200:


                data = response.json()



                forecast_text = f"""
5-Day forecast for {city}:

"""


                for item in data["list"][::8]:


                    forecast_text += f"""
📅 {item['dt_txt']}

🌡 {item['main']['temp']} °C

☁ {item['weather'][0]['description'].title()}


"""


                bot_response = generate_response(
                    user_query=user_input,
                    weather_data={
                        "name": city,
                        "main":{
                            "temp": data["list"][0]["main"]["temp"],
                            "feels_like": data["list"][0]["main"]["feels_like"],
                            "humidity": data["list"][0]["main"]["humidity"]
                        },
                        "weather": data["list"][0]["weather"],
                        "wind":{
                            "speed": data["list"][0]["wind"]["speed"]
                        }
                    }
                ) + "\n\n" + forecast_text



            else:

                bot_response = "Forecast data not available."



    else:

        bot_response = "Please ask something related to weather."





    # Show Assistant Response

    with st.chat_message("assistant"):

        st.write(bot_response)



    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":bot_response
        }
    )