import streamlit as st
from weather_api import get_current_weather, get_forecast
from utils import extract_city


# Page Setup
st.set_page_config(
    page_title="AI Weather Chatbot",
    page_icon="🌦️"
)


# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []


# UI Styling
st.markdown("""
<style>

.main {
    background-color: #f5f9ff;
}

h1 {
    text-align: center;
}

.weather-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)



# Title
st.title("🌦️ AI Weather Chatbot")
st.caption("Ask current weather or 5-day forecast")



# Chat History
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])




# User Input
user_input = st.chat_input(
    "Example: Lahore weather / Lahore forecast"
)



if user_input:


    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    with st.chat_message("user"):
        st.write(user_input)



    # Extract City

    city = extract_city(user_input)

   



    request_type = user_input.lower()



    # Current Weather

    if (
        "weather" in request_type
        or "temperature" in request_type
        or "current" in request_type
    ):


        response = get_current_weather(city)


        if response.status_code == 200:


            data = response.json()
            # st.write(data["coord"])
            # st.write(data["main"])
            # st.write(data["weather"])


            bot_response = f"""
🌍 City: {data['name']}

🌡 Temperature: {data['main']['temp']} °C

☁ Condition: {data['weather'][0]['description'].title()}

💧 Humidity: {data['main']['humidity']}%

💨 Wind Speed: {data['wind']['speed']} m/s
"""


            with st.chat_message("assistant"):

                st.info(bot_response)



            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": bot_response
                }
            )



        else:

            st.error("City not found")




    # Forecast

    elif (
        "forecast" in request_type
        or "5" in request_type
        or "future" in request_type
    ):



        response = get_forecast(city)



        if response.status_code == 200:


            data = response.json()


            st.subheader("📅 5-Day Forecast")



            for item in data["list"][::8]:


                st.info(
                    f"""
📆 Date: {item['dt_txt']}

🌡 Temperature: {item['main']['temp']} °C

☁ Condition: {item['weather'][0]['description'].title()}
"""
                )



        else:

            st.error("Forecast not found")



    else:


        st.warning(
            "Please ask like: Lahore weather or Lahore forecast"
        )