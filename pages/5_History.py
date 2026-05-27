from datetime import datetime, timedelta
import os
import streamlit as st
from PIL import Image

from utils.ui import load_ui, sidebar
from utils.database import (
    get_user_predictions,
    delete_prediction
)

st.set_page_config(
    page_title="History",
    page_icon="📜",
    layout="wide"
)

if not st.session_state.get("logged_in"):
    st.switch_page("pages/1_Login.py")

load_ui()
sidebar()

st.markdown("""
<style>

.history-title{
    font-size:58px;
    font-weight:800;
    background:linear-gradient(90deg,#60a5fa,#3b82f6);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:0;
}

.history-subtitle{
    color:#cbd5e1;
    font-size:20px;
    margin-top:-10px;
    margin-bottom:35px;
}

.result-container{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:20px;
    padding:20px;
    margin-bottom:20px;
}

.stButton > button{
    border-radius:14px;
    font-weight:700;
    border:none;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='history-title'>
📜 History
</div>

<div class='history-subtitle'>
Riwayat hasil deteksi AI anime character
</div>
""", unsafe_allow_html=True)

username = st.session_state.username

history = get_user_predictions(username)

if not history:

    st.warning(
        "Belum ada history prediction."
    )

else:

    for row in history:

        prediction_id = row[0]
        prediction = row[2]
        confidence = row[3]
        image_path = row[4]

        col1, col2 = st.columns([1, 1.5])

        with col1:

            if os.path.exists(image_path):

                image = Image.open(image_path)

                st.image(
                    image,
                    width=240
                )

        with col2:

            st.markdown(
                "<div class='result-container'>",
                unsafe_allow_html=True
            )

            st.subheader(f"🌸 {prediction}")

            st.success(
                f"Confidence: {confidence:.2f}%"
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

            if st.button(
                f"🗑️ Hapus",
                key=f"delete_{prediction_id}"
            ):

                st.session_state["selected_delete_id"] = prediction_id
                st.session_state["selected_delete_image"] = image_path

        st.markdown("<br>", unsafe_allow_html=True)

if "selected_delete_id" in st.session_state:

    selected_id = st.session_state["selected_delete_id"]
    selected_image = st.session_state["selected_delete_image"]

    @st.dialog("⚠️ Konfirmasi Hapus")
    def confirm_delete():

        st.warning(
            f"Yakin mau hapus Prediction?"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "✅ Ya"
            ):

                delete_prediction(selected_id)

                if os.path.exists(selected_image):

                    os.remove(selected_image)

                del st.session_state["selected_delete_id"]
                del st.session_state["selected_delete_image"]

                st.success(
                    "History berhasil dihapus."
                )

                st.rerun()

        with col2:

            if st.button(
                "❌ Batal"
            ):

                del st.session_state["selected_delete_id"]
                del st.session_state["selected_delete_image"]

                st.rerun()

    confirm_delete()
