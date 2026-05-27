from datetime import datetime

import streamlit as st

from utils.auth import register_user
from utils.ui import load_ui

st.set_page_config(
    page_title="Register",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_ui()

st.markdown("""
<div style='text-align:center;padding-top:80px'>

<div class='title'>
🌸 Waifugram AI
</div>

<div class='subtitle'>
Create New Account
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.2, 1])

with col2:

    username = st.text_input("Username")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button(
        "Register",
        use_container_width=True
    ):

        if password != confirm:

            st.error(
                "Password tidak sama"
            )

        else:

            register_user(
                username,
                email,
                password
            )

            st.session_state.logged_in = True

            st.session_state.username = username

            st.session_state.last_activity = datetime.now()

            st.success(
                "Register berhasil!"
            )

            st.switch_page("pages/3_Dashboard.py")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "Sudah punya akun? Login",
        use_container_width=True
    ):

        st.switch_page("pages/1_Login.py")