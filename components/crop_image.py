import os
import streamlit as st


def show_crop_image(crop_name):
    """
    Display crop image from assets/crops folder.

    Example:
    assets/
        crops/
            rice.png
            maize.png
            coffee.png
    """

    # Project root directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Image path
    image_path = os.path.join(
        BASE_DIR,
        "assets",
        "crops",
        f"{crop_name.lower()}.png"
    )

    # Check if image exists
    if os.path.exists(image_path):

        st.image(
            image_path,
            caption=crop_name.title(),
            width=300
        )

    else:

        st.warning(f"⚠️ Image not found: {crop_name}.png")