from datetime import datetime, timedelta

import streamlit as st

from utils.auth import login_user
from utils.ui import load_ui

st.set_page_config(
    page_title="Login",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_ui()

if "last_activity" not in st.session_state:

    st.session_state.last_activity = datetime.now()

else:

    now = datetime.now()

    timeout = timedelta(minutes=5)

    if now - st.session_state.last_activity > timeout:

        st.session_state.clear()

    else:

        st.session_state.last_activity = now

st.markdown("""
<div style='text-align:center;padding-top:80px'>

<div class='title'>
🌸 Waifugram AI
</div>

<div class='subtitle'>
AI Anime Character Detection System
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.2, 1])

with col2:

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        role = login_user(
            username,
            password
        )

        if role:

            st.session_state.logged_in = True

            st.session_state.username = username

            st.session_state.role = role

            st.session_state.last_activity = datetime.now()

            st.success(
                "Login berhasil!"
            )

            st.switch_page("pages/3_Dashboard.py")

        else:

            st.error(
                "Username atau password salah"
            )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "Belum punya akun? Register",
        use_container_width=True
    ):

        st.switch_page("pages/2_Register.py")