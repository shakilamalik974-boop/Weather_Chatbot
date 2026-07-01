import os
import json
from groq import Groq
from dotenv import load_dotenv


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def extract_intent(user_query):

    prompt = f"""
You are an AI assistant that extracts information for a weather chatbot.

Analyze the user query and return ONLY valid JSON.
No explanation.
No markdown.

Extract:

intent:
- current_weather
- forecast
- not_weather

city:
- city name only
- if no city found, return empty string

time:
- today
- tomorrow
- yesterday
- unknown



User query:
{user_query}


Example:

User:
How is the weather in Lahore today?

Return:

{{
"intent":"current_weather",
"city":"Lahore",
"time":"today"
}}

"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )


    result = response.choices[0].message.content


    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()


    return json.loads(result)





def generate_response(user_query, weather_data):


    prompt = f"""

You are a friendly AI Weather Assistant.

Your job is to answer weather-related questions.

User asked:
{user_query}


Weather data:

City:
{weather_data['name']}

Temperature:
{weather_data['main']['temp']} °C

Feels like:
{weather_data['main']['feels_like']} °C

Humidity:
{weather_data['main']['humidity']}%

Condition:
{weather_data['weather'][0]['description']}

Wind speed:
{weather_data['wind']['speed']} m/s


Instructions:

- Answer naturally like a human.
- Keep response clear and helpful.
- Give small recommendations when useful.
- Do not mention APIs.
- Do not mention JSON.
- Do not say you are an AI model.
- Answer according to user's question.
- If user asks only temperature, only give temperature.
- If user asks humidity, only give humidity.
- Keep answers short (2-4 lines).
- Give recommendations only if user asks.
- Do not repeat all weather details every time.


"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )


    return response.choices[0].message.content