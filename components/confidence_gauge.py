import streamlit as st
import plotly.graph_objects as go


def show_confidence_gauge(confidence):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=confidence,
            number={"suffix": "%"},
            title={"text": "AI Confidence"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#22C55E"},
                "steps": [
                    {"range": [0, 50], "color": "#334155"},
                    {"range": [50, 80], "color": "#475569"},
                    {"range": [80, 100], "color": "#22C55E"},
                ],
            },
        )
    )

    fig.update_layout(
        height=330,
        paper_bgcolor="#0F172A",
        font=dict(color="white"),
        margin=dict(l=20, r=20, t=50, b=20),
    )

    st.plotly_chart(fig, use_container_width=True)