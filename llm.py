import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def chat_with_llm(user_query, weather_data=None, chat_history=None):
    """
    Single intelligent brain for everything
    """

    system_prompt = """
You are a high-accuracy AI Weather Assistant.

Your job is ONLY to provide weather-related information.

========================
CORE RULES
========================

1. ONLY answer weather-related queries:
   - weather conditions
   - temperature
   - humidity
   - wind
   - rain prediction
   - umbrella/jacket advice
   - forecasts

2. If user asks NON-weather questions:
   Politely respond:
   "I can only help with weather-related questions."

3. NEVER guess or hallucinate:
   - If weather data is not provided, say:
     "I don't have enough weather data for this location."

4. ALWAYS use provided weather data when available.
   Do NOT assume values.

5. If user asks follow-up questions (e.g. "humidity", "what about tomorrow", "should I carry umbrella"):
   - Use last provided weather context
   - Do NOT ask user to repeat city

6. Keep responses:
   - Short (2–5 lines max)
   - Clear
   - Natural human tone
   - No unnecessary explanations

7. Recommendations rules:
   - Umbrella → only if rain probability or cloudy/rain condition exists
   - Heat advice → only if temp > 32°C
   - Cold advice → only if temp < 15°C

8. If city is missing:
   Try to use previous conversation context.
   If still unknown, ask:
   "Please tell me the city you want weather for."

========================
OUTPUT STYLE
========================

- No JSON
- No technical language
- No API mentions
- No long paragraphs
- Direct answers only
"""

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    if chat_history:
        messages.extend(chat_history[-6:])  # memory (last 6 messages)

    user_content = user_query

    if weather_data:
        user_content += f"""

Weather Data:
City: {weather_data.get('name')}
Temperature: {weather_data['main']['temp']}°C
Feels Like: {weather_data['main']['feels_like']}°C
Humidity: {weather_data['main']['humidity']}%
Condition: {weather_data['weather'][0]['description']}
Wind: {weather_data['wind']['speed']} m/s
"""

    messages.append({"role": "user", "content": user_content})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.6
    )

    return response.choices[0].message.content