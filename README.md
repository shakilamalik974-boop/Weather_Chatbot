# 🌦️ AI Weather Chatbot

## 📌 Project Overview

AI Weather Chatbot is a Python-based chatbot application developed using Streamlit.  
The purpose of this project is to provide real-time weather information and future weather forecasts by interacting with users in a simple chat interface.

The chatbot uses OpenWeatherMap REST API to fetch weather data and displays current weather details and 5-day forecasts based on the user's city input.

---

## ✨ Features

### 🌡️ Current Weather Information
The chatbot provides:

- City name
- Current temperature
- Weather condition
- Humidity percentage
- Wind speed


### 📅 5-Day Weather Forecast

Users can request future weather predictions, and the chatbot displays:

- Date and time
- Temperature
- Weather condition


### 💬 Chat Interface

- User-friendly chatbot style interface
- Maintains conversation history during the session
- Accepts natural user queries like:
  - Lahore weather
  - Lahore forecast


### 🔐 Secure API Handling

- API key is stored securely using `.env` file
- Sensitive information is not directly written in the source code


---

# 🛠️ Technologies Used

## Programming Language

**Python**

Used for:
- Backend logic
- API handling
- Data processing


## Frontend Framework

**Streamlit**

Used for:
- Creating chatbot interface
- Displaying weather information
- Building interactive UI


## API Integration

**OpenWeatherMap REST API**

Used to:
- Fetch current weather data
- Fetch 5-day weather forecast


## Libraries

### Requests

Used for sending HTTP GET requests to the weather API.


### python-dotenv

Used for loading environment variables securely from `.env` file.


---

# 🔄 Working Flow

The complete workflow of the application:

1. User enters a weather query.

Example: Lahore Weather

2. Application extracts the city name from user input.

3. Python sends a GET request to OpenWeatherMap REST API.

4. API processes the request and returns weather information in JSON format.

5. Python converts the JSON response into usable data.

6. Required information is extracted and displayed on the Streamlit interface.

---

# 🌐 REST API Integration

This project uses REST API architecture.

## Current Weather Endpoint

https://api.openweathermap.org/data/2.5/weather

Used for fetching current weather details.


## Forecast Endpoint

https://api.openweathermap.org/data/2.5/forecast

Used for retrieving 5-day weather forecast

### app.py

Main application file containing:
- Streamlit UI
- API requests
- Weather processing logic


### .env

Stores API key securely.

Example: OPENWEATHER_API_KEY=your_api_key

### requirements.txt

Contains required Python packages.


---

# ⚙️ Installation & Setup

## Step 1: Clone or Download Project

Download the project files.


## Step 2: Install Dependencies

Run: pip install -r requirements.txt

## Step 3: Configure API Key

Create a `.env` file: OPENWEATHER_API_KEY=your_api_key

## Step 4: Run Application

Start Streamlit: streamlit run app.py

---

# 📌 API Response Handling

The application checks HTTP status codes:

### 200

Request successful and weather data received.


### 401

Invalid API key.


### 404

City not found.


---

# 🎯 Project Objective

The main objective of this project is to understand:

- REST API integration
- HTTP GET requests
- JSON data handling
- Environment variables
- Streamlit application development


---

# 👩‍💻 Development Tools

- Visual Studio Code
- Python
- Streamlit
- OpenWeatherMap API


---

# Conclusion

AI Weather Chatbot successfully demonstrates how a Python application can communicate with external REST APIs, process real-time data, and provide interactive results through a user-friendly chatbot interface.
