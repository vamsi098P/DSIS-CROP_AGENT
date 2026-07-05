import streamlit as st


def show_header():

    st.markdown(
        """
        <div style="
            background: linear-gradient(90deg,#14532d,#166534,#15803d);
            padding:30px;
            border-radius:18px;
            color:Dark white;
            text-align:center;
            margin-bottom:20px;
        ">

        <h1>🌾 DSIS CROPAGENT</h1>

        <h4>
        Intelligent Crop Recommendation & Smart Farming Assistant
        </h4>

        </div>
        """,
        unsafe_allow_html=True
    )