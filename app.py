import streamlit as st
import pandas as pd

from core.agent_service import AgriMindAgent

from services.pdf_service import PDFService
from services.history_service import HistoryService

from components.custom_css import load_css
from components.header import show_header
from components.sidebar import show_sidebar
from components.input_form import show_input_form
from components.result_cards import show_result
from components.weather_card import show_weather_card


# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="AgriMind AI",
    page_icon="🌾",
    layout="wide"
)

# =====================================================
# Load UI
# =====================================================

load_css()

show_sidebar()

show_header()

# =====================================================
# Initialize Services
# =====================================================

agent = AgriMindAgent()

pdf_service = PDFService()

history = HistoryService()

# =====================================================
# Input Form
# =====================================================

(
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
) = show_input_form()

# =====================================================
# Live Weather Card
# =====================================================

if weather:

    show_weather_card(weather)

# =====================================================
# AI Prediction
# =====================================================

if predict:

    with st.spinner("🤖 AgriMind AI is analyzing your farm..."):

        result = agent.analyze(
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        )

    # ================================================
    # Show Results
    # ================================================

    show_result(result)

    # ================================================
    # Save Prediction History
    # ================================================

    history.save_prediction(
        city=city,
        crop=result["recommended_crop"],
        confidence=result["confidence"]
    )

    # ================================================
    # Default Weather (if user didn't fetch weather)
    # ================================================

    if weather is None:

        weather = {

            "city": city,

            "country": "Unknown",

            "temperature": temperature,

            "humidity": humidity,

            "rainfall": rainfall,

            "wind_speed": "-",

            "condition": "Not Available"

        }

    # ================================================
    # Generate PDF
    # ================================================

    pdf_path = pdf_service.generate_report(
        result=result,
        weather=weather
    )

    # ================================================
    # Download PDF
    # ================================================

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            label="📄 Download AI Report",
            data=pdf_file,
            file_name="AgriMind_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# =====================================================
# Prediction History
# =====================================================

st.markdown("---")

st.subheader("📜 Prediction History")

history_data = history.get_history()

if history_data:

    df = pd.DataFrame(
        history_data,
        columns=[
            "Date",
            "City",
            "Recommended Crop",
            "Confidence (%)"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No prediction history available.")
   
# =====================================================
# Developer Footer
# =====================================================

st.markdown("---")

st.markdown(
    """
    <style>
    .developer-footer{
        background:#111827;
        padding:25px;
        border-radius:15px;
        text-align:center;
        border-top:4px solid #22C55E;
        margin-top:30px;
    }

    .developer-footer h3{
        color:#22C55E;
        margin-bottom:10px;
    }

    .developer-footer h4{
        color:white;
        margin-bottom:5px;
    }

    .developer-footer p{
        color:#D1D5DB;
        margin:4px;
    }

    .developer-footer a{
        color:#60A5FA;
        text-decoration:none;
    }
    </style>

    <div class="developer-footer">

    <h3>👨‍💻 Developed By</h3>

    <h4>Vamsi Garapati</h4>

    <p>B.Tech – Computer Science & Data Science</p>

    <p>NRI Institute of Technology</p>

    <p>📧 vamsigarapati40@gmail.com</p>

    <p>
        💼
        <a href="https://www.linkedin.com/in/vamsi-garapati-36ab4632b" target="_blank">
        LinkedIn
        </a>

        

        

    

    <p>🌾 DSIS CROP AGENT v1.0</p>

    <p>AI-Powered Smart Crop Recommendation System</p>

    </div>
    """,
    unsafe_allow_html=True
)