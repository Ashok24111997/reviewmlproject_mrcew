import streamlit as st
import requests


st.set_page_config(page_title="Weather App", page_icon="🌦", layout="centered")


st.sidebar.title("🌍 Weather App")
city = st.sidebar.text_input("Enter City Name")

API_KEY = "1c44ee146ad74caeb1e173037262303"

# Title
st.title("🌦 Weather Dashboard")

if city:
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    try:
        with st.spinner("Fetching weather..."):
            response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

          
            location = data["location"]["name"]
            country = data["location"]["country"]
            temp = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind = data["current"]["wind_kph"]

            # 📍 Location
            st.subheader(f"📍 {location}, {country}")

            # 🌡 Temperature & Condition
            st.write(f"🌡 Temperature: **{temp} °C**")
            st.write(f"🌥 Condition: **{condition}**")

            # 📊 Metrics (Nice UI)
            col1, col2 = st.columns(2)

            col1.metric("💧 Humidity", f"{humidity}%")
            col2.metric("💨 Wind Speed", f"{wind} kph")

        else:
            st.error("❌ City not found or API issue")

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("👈 Enter a city name from the sidebar")