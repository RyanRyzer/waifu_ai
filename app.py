import streamlit as st

st.set_page_config(
    page_title="Waifugram AI",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.logged_in:
    st.switch_page("pages/3_Dashboard.py")
else:
    st.switch_page("pages/1_Login.py")