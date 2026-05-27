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

now = datetime.now()

timeout = timedelta(minutes=5)

if "last_activity" in st.session_state:

    if now - st.session_state.last_activity > timeout:

        st.session_state.clear()

        st.warning(
            "Session expired."
        )

        st.switch_page("pages/1_Login.py")

    else:

        st.session_state.last_activity = now

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

.stProgress > div > div{
    background:linear-gradient(90deg,#2563eb,#60a5fa);
}

.stButton > button{
    border-radius:14px;
    font-weight:700;
    border:none;
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

    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )

    UPLOAD_DIR = os.path.join(
        BASE_DIR,
        "..",
        "uploads"
    )

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True
    )

    filename = f"{uuid.uuid4()}.png"

    filepath = os.path.join(
        UPLOAD_DIR,
        filename
    )

    image.save(filepath)

    filepath = os.path.abspath(filepath)

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
            width=320
        )

    with col2:

        st.success(
            f"🌸 Prediction: {label}"
        )

        st.info(
            f"Confidence: {confidence:.2f}%"
        )

        st.subheader(
            "🏆 Top 3 Predictions"
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

            st.write(
                f"### {category}"
            )

            st.caption(
                f"{score:.2f}%"
            )

            st.progress(
                min(int(score), 100)
            )

            st.markdown("<br>", unsafe_allow_html=True)