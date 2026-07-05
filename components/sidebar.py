import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.image(
            "assets/logo.png",
            width=140
        )

        st.markdown(
            "<h2 style='text-align:center;'>AgriMind AI</h2>",
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.success("🌾 Crop Recommendation")

        st.success("🤖 Gemini AI")

        st.success("🌦 Live Weather")

        st.success("🌱 Fertilizer Advice")

        st.success("💧 Irrigation Guide")

        st.success("📄 PDF Report")

        st.success("🗄 Prediction History")

        st.markdown("---")

        st.info("🚀 Version 1.0")

        st.caption("Developed by Vamsi Garapati")