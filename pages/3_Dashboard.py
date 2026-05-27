import os
import streamlit as st
from PIL import Image

from utils.ui import load_ui, sidebar
from utils.database import (
    get_total_users,
    get_total_predictions,
    get_latest_predictions,
    reset_history
)

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

if not st.session_state.get("logged_in"):
    st.switch_page("pages/1_Login.py")

load_ui()
sidebar()

total_users = get_total_users()

total_predictions = get_total_predictions()

latest_predictions = get_latest_predictions()

st.title("Dashboard")

st.caption(
    "AI Anime Character Detection System"
)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    with st.container(border=True):

        st.metric(
            "🎯 Total Predictions",
            total_predictions
        )

with col2:

    with st.container(border=True):

        st.metric(
            "👥 Total Users",
            total_users
        )

with col3:

    with st.container(border=True):

        st.metric(
            "🤖 AI Model",
            "TF Lite"
        )

st.markdown("<br><br>", unsafe_allow_html=True)

top1, top2 = st.columns([5, 1])

with top1:

    st.subheader(
        "🌸 Latest Community Predictions"
    )

with top2:

    if st.session_state.get("role") == "admin":

        if st.button(
            "🗑️ Reset Feed",
            use_container_width=True
        ):

            reset_history()

            st.success(
                "Community feed berhasil direset."
            )

            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

if latest_predictions:

    cols = st.columns(3)

    for index, row in enumerate(latest_predictions):

        username = row[0]
        prediction = row[1]
        confidence = row[2]
        image_path = row[3]

        with cols[index % 3]:

            with st.container(border=True):

                if image_path and os.path.exists(image_path):

                    image = Image.open(image_path)

                    st.image(
                        image,
                        width=240
                    )

                st.info(
                    f"👤 User: {username}"
                )

                st.success(
                    f"🌸 Prediction: {prediction}"
                )

                st.warning(
                    f"Confidence: {confidence:.2f}%"
                )

else:

    st.info(
        "Belum ada community prediction."
    )