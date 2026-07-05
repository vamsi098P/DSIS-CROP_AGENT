import streamlit as st
import google.generativeai as genai


class GeminiService:

    def __init__(self):

        genai.configure(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        # Stable model
        self.model = genai.GenerativeModel("gemini-1.5-flash")

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

        try:

            response = self.model.generate_content(prompt)

            if response and hasattr(response, "text"):
                return response.text

            return "AI explanation is currently unavailable."

        except Exception:

            return f"""
🌾 **AI Recommendation**

Based on the soil nutrients and weather conditions, **{crop.title()}** is the most suitable crop for your farm.

**Prediction Confidence:** {confidence:.1f}%

### 🌱 Recommended Fertilizers
• {', '.join(fertilizer["fertilizers"])}

### 💧 Irrigation Advice
• Method: {irrigation["method"]}

• Frequency: {irrigation["frequency"]}

• Water Requirement: {irrigation["water_requirement"]}

The AI explanation service is temporarily unavailable due to API quota or connectivity issues.

The crop recommendation, fertilizer suggestion, and irrigation advice above are still generated using the trained Machine Learning model and rule-based agricultural knowledge.
"""