from datetime import datetime, timedelta
import streamlit as st

from utils.ui import load_ui, sidebar
from utils.database import (
    get_total_users,
    get_total_predictions
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

st.markdown("""
<div class='title'>
Dashboard
</div>

<div class='subtitle'>
AI Anime Character Detection System
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        f"""
        <div class='glass'>
            <h1>{total_predictions}</h1>
            <p>Total Prediction</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        f"""
        <div class='glass'>
            <h1>{total_users}</h1>
            <p>Total Users</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown("""
    <div class='glass'>
        <h1>TensorFlow Lite</h1>
        <p>AI Model</p>
    </div>
    """, unsafe_allow_html=True)