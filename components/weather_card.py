import streamlit as st


def show_weather_card(weather):

    if weather is None:
        return

    st.markdown("## 🌦 Live Weather")

    with st.container(border=True):

        col1, col2 = st.columns([1, 4])

        with col1:
            st.image(weather["icon"], width=90)

        with col2:

            st.markdown(
                f"""
                ### 📍 {weather['city']}, {weather['country']}

                **☁ {weather['condition']}**
                """
            )

        st.markdown("---")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "🌡 Temperature",
                f"{weather['temperature']}°C"
            )

       