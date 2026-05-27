import streamlit as st


def load_ui():

    st.markdown("""
    <style>

    #MainMenu{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    header{
        background:transparent !important;
    }

    [data-testid="stHeader"]{
        background:transparent !important;
    }

    .stApp{
        background:
        linear-gradient(
        90deg,
        #020617 0%,
        #00113a 45%,
        #111827 100%
        );
        color:white;
    }

    section[data-testid="stSidebar"]{
        background:
        linear-gradient(
        180deg,
        #081129 0%,
        #0f172a 100%
        );
        border-right:1px solid rgba(255,255,255,0.08);
    }

    .block-container{
        padding-top:2rem;
    }

    .title{
        font-size:64px;
        font-weight:800;
        background:linear-gradient(
        90deg,
        #60a5fa,
        #3b82f6
        );
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    .subtitle{
        color:#d1d5db;
        font-size:22px;
        margin-top:-15px;
        margin-bottom:35px;
    }

    .glass{
        background:rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.08);
        backdrop-filter:blur(14px);
        border-radius:24px;
        padding:20px;
    }

    .metric-card{
        background:rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:24px;
        padding:35px;
        backdrop-filter:blur(14px);
    }

    .stButton button{
        width:100%;
        background:linear-gradient(
        90deg,
        #2563eb,
        #3b82f6
        )!important;

        color:white!important;
        border:none!important;
        border-radius:14px!important;
        padding:14px 18px!important;
        font-weight:700!important;
    }

    .stTextInput input{
        background:rgba(255,255,255,0.05)!important;
        border:1px solid rgba(255,255,255,0.08)!important;
        color:white!important;
        border-radius:14px!important;
    }

    div[data-testid="collapsedControl"]{
        position:fixed !important;
        top:14px !important;
        left:14px !important;
        z-index:999999 !important;
    }

    div[data-testid="collapsedControl"] button{
        background:rgba(15,23,42,0.95)!important;
        border:1px solid rgba(255,255,255,0.08)!important;
        border-radius:12px!important;
        width:46px!important;
        height:46px!important;
    }

    div[data-testid="collapsedControl"] button:hover{
        background:#2563eb!important;
    }

    div[data-testid="collapsedControl"] svg{
        width:22px!important;
        height:22px!important;
        color:white!important;
    }

    [data-testid="stSidebarNav"]{
        display:none !important;
    }

    </style>
    """, unsafe_allow_html=True)


def sidebar():

    with st.sidebar:

        st.markdown("# 🌸 Waifugram")

        st.divider()

        st.markdown("## 🚀 Navigation")

        st.page_link(
            "pages/3_Dashboard.py",
            label="🏠 Dashboard"
        )

        st.page_link(
            "pages/4_AI_Detection.py",
            label="🎯 AI Detection"
        )

        st.page_link(
            "pages/5_History.py",
            label="📜 History"
        )

        st.page_link(
            "pages/6_About.py",
            label="ℹ️ About"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        username = st.session_state.get(
            "username",
            "admin"
        )

        st.info(f"👤 Login sebagai:\n\n{username}")

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.switch_page(
                "pages/1_Login.py"
            )