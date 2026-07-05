import streamlit as st
from components.crop_image import show_crop_image
from components.confidence_gauge import show_confidence_gauge


def show_result(result):

    crop = result["recommended_crop"]
    confidence = result["confidence"]
    fertilizer = result["fertilizer"]
    irrigation = result["irrigation"]
    ai_explanation = result["ai_explanation"]

    st.success("✅ AI Analysis Completed Successfully")

    st.markdown("---")

    # ===================================================
    # TOP SECTION
    # ===================================================

    left, right = st.columns([1, 1])

    # ===================================================
    # Crop Card
    # ===================================================

    with left:

        st.markdown("## 🌾 Recommended Crop")

        with st.container(border=True):

            show_crop_image(crop)

            st.markdown(
                f"""
                <h2 style="text-align:center;">
                    🌾 {crop.title()}
                </h2>
                """,
                unsafe_allow_html=True
            )

            if confidence >= 90:
                st.success("🏆 Excellent Match")
            elif confidence >= 75:
                st.info("✅ Good Match")
            else:
                st.warning("⚠ Moderate Match")

            st.metric(
                label="AI Confidence",
                value=f"{confidence:.1f}%"
            )

    # ===================================================
    # Confidence Gauge
    # ===================================================

    with right:

        st.markdown("## 📊 AI Confidence")

        with st.container(border=True):

            show_confidence_gauge(confidence)

    st.markdown("---")

    # ===================================================
    # Fertilizer Recommendation
    # ===================================================

    st.markdown("## 🌱 Fertilizer Recommendation")

    with st.container(border=True):

        st.subheader("Recommended Fertilizers")

        for item in fertilizer["fertilizers"]:
            st.success(f"✅ {item}")

        if "application_stage" in fertilizer:

            st.subheader("Application Stage")

            for stage in fertilizer["application_stage"]:
                st.info(stage)

        st.subheader("Description")

        st.write(fertilizer["description"])

    st.markdown("---")

    # ===================================================
    # Irrigation Recommendation
    # ===================================================

    st.markdown("## 💧 Irrigation Recommendation")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            label="🚿 Method",
            value=irrigation["method"]
        )

    with col2:

        st.metric(
            label="📅 Frequency",
            value=irrigation["frequency"]
        )

    with col3:

        st.metric(
            label="💦 Water Requirement",
            value=irrigation["water_requirement"]
        )

    st.info(irrigation["description"])

    st.markdown("---")

    # ===================================================
    # Gemini AI Recommendation
    # ===================================================

    st.markdown("## 🤖 AI Expert Recommendation")

    with st.container(border=True):

        st.markdown(
            f"""
<div style="
background:#17233A;
padding:25px;
border-radius:15px;
border-left:6px solid #22C55E;
font-size:16px;
line-height:1.8;
">

<h3>🌾 Personalized AI Recommendation</h3>

{ai_explanation}

</div>
""",
            unsafe_allow_html=True
        )