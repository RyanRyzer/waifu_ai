from datetime import datetime, timedelta
import os
import uuid
import streamlit as st
from PIL import Image

from utils.ui import load_ui, sidebar
from utils.prediction import predict_image
from utils.database import save_prediction

st.set_page_config(
    page_title="AI Detection",
    page_icon="🎯",
    layout="wide"
)

if not st.session_state.get("logged_in"):
    st.switch_page("pages/1_Login.py")

load_ui()
sidebar()

st.markdown("""
<style>

.detect-title{
    font-size:58px;
    font-weight:800;
    background:linear-gradient(90deg,#60a5fa,#3b82f6);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:0;
}

.detect-subtitle{
    color:#cbd5e1;
    font-size:20px;
    margin-top:-10px;
    margin-bottom:35px;
}

.result-card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:24px;
    padding:28px;
    margin-top:10px;
}

.result-label{
    font-size:42px;
    font-weight:800;
    color:white;
    margin-bottom:18px;
}

.result-confidence{
    font-size:24px;
    font-weight:700;
    color:#4ade80;
}

.top-title{
    font-size:28px;
    font-weight:800;
    color:white;
    margin-top:24px;
    margin-bottom:18px;
}

.prediction-name{
    font-size:18px;
    font-weight:700;
    color:white;
    margin-bottom:5px;
}

.prediction-score{
    color:#60a5fa;
    font-weight:700;
    margin-bottom:10px;
}

.stProgress > div > div{
    background:linear-gradient(90deg,#2563eb,#60a5fa);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='detect-title'>
🎯 AI Detection
</div>

<div class='detect-subtitle'>
Upload gambar anime untuk dideteksi oleh AI
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload Anime Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    filename = f"{uuid.uuid4()}.png"

    filepath = os.path.join(
        "uploads",
        filename
    )

    image.save(filepath)

    label, confidence, output = predict_image(image)

    save_prediction(
        st.session_state.username,
        label,
        confidence,
        filepath
    )

    col1, col2 = st.columns([1, 1.4])

    with col1:

        st.image(
            image,
            width=340
        )

    with col2:

        st.markdown(
            """
            <div class='result-card'>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class='result-label'>
                🌸 {label}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class='result-confidence'>
                Confidence: {confidence:.2f}%
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class='top-title'>
                🏆 Top 3 Predictions
            </div>
            """,
            unsafe_allow_html=True
        )

        categories = [
            "Maid",
            "Cat Girl",
            "Elf",
            "Furry",
            "Loli",
            "Game",
            "Teen",
            "Milf"
        ]

        results = []

        for i in range(len(categories)):

            score = float(output[i]) * 100

            results.append(
                (
                    categories[i],
                    score
                )
            )

        results.sort(
            key=lambda x: x[1],
            reverse=True
        )

        top_results = results[:3]

        for category, score in top_results:

            st.markdown(
                f"""
                <div class='prediction-name'>
                    {category}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class='prediction-score'>
                    {score:.2f}%
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(
                min(int(score), 100)
            )

            st.markdown("<br>", unsafe_allow_html=True)