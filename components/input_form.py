import streamlit as st
from services.weather_service import WeatherService


def show_input_form():

    st.subheader("🌱 Enter Soil & Weather Details")

    weather_service = WeatherService()

    # =====================================
    # Session State
    # =====================================

    if "weather" not in st.session_state:
        st.session_state.weather = None

    # =====================================
    # City
    # =====================================

    city = st.text_input(
        "📍 City",
        value="Vijayawada"
    )

    if st.button("🌦 Get Live Weather"):

        weather = weather_service.get_weather(city)

        if weather:

            st.session_state.weather = weather

            st.success(f"Weather loaded for {weather['city']}")

        else:

            st.error("Unable to fetch weather.")

    weather = st.session_state.weather

    st.markdown("---")

    col1, col2 = st.columns(2)

    # =====================================
    # Soil
    # =====================================

    with col1:

        nitrogen = st.number_input(
            "Nitrogen (N)",
            0,
            150,
            90
        )

        phosphorus = st.number_input(
            "Phosphorus (P)",
            0,
            150,
            42
        )

        potassium = st.number_input(
            "Potassium (K)",
            0,
            250,
            43
        )

        ph = st.number_input(
            "Soil pH",
            0.0,
            14.0,
            6.5
        )

    # =====================================
    # Weather
    # =====================================

    with col2:

        if weather:

            temperature = st.number_input(
                "Temperature (°C)",
                value=float(weather["temperature"])
            )

            humidity = st.number_input(
                "Humidity (%)",
                value=float(weather["humidity"])
            )

            rainfall = st.number_input(
                "Rainfall (mm)",
                value=float(weather["rainfall"])
            )

            st.info(f"☁ {weather['condition']}")

        else:

            temperature = st.number_input(
                "Temperature (°C)",
                value=20.0
            )

            humidity = st.number_input(
                "Humidity (%)",
                value=82.0
            )

            rainfall = st.number_input(
                "Rainfall (mm)",
                value=202.0
            )

    st.markdown("---")

    predict = st.button(
        "🚀 Predict Crop",
        use_container_width=True
    )

    return (
        city,
        weather,
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall,
        predict
    )