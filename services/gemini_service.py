import streamlit as st
import google.generativeai as genai


class GeminiService:

    def __init__(self):

        genai.configure(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_explanation(
        self,
        crop,
        confidence,
        fertilizer,
        irrigation,
    ):

        prompt = f"""
You are an agricultural expert.

Crop Recommendation:
{crop}

Confidence:
{confidence:.1f}%

Recommended Fertilizers:
{', '.join(fertilizer["fertilizers"])}

Irrigation Method:
{irrigation["method"]}

Frequency:
{irrigation["frequency"]}

Water Requirement:
{irrigation["water_requirement"]}

Write a professional explanation for a farmer.

Include:
1. Why this crop is recommended.
2. Benefits of the fertilizers.
3. Irrigation advice.
4. Keep the explanation under 150 words.
5. Use simple English.
"""

        response = self.model.generate_content(prompt)

        return response.text