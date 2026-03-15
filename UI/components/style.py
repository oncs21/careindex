import streamlit as st

def apply_styles():

    st.markdown("""
    <style>
                
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
                
    [data-testid="stSidebarNav"] {
        display: none;
    }

    .stApp {
        background-color: #f6f8fb;
    }


    header {visibility: hidden;}


    .navbar {
        background: white;
        padding: 12px 24px;
        border-bottom: 1px solid #e6e8eb;
        border-radius: 8px;
    }


    section[data-testid="stSidebar"] {
        background-color: white;
        border-right: 1px solid #e6e8eb;
    }


    h1 {
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    h2 {
        font-weight: 600;
    }


    .card {
        background: white;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #e8eaef;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .card:hover {
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        transform: translateY(-2px);
    }


    .patient-header {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e8eaef;
    }


    input {
        border-radius: 10px !important;
    }


    .stButton button {
        border-radius: 8px;
        padding: 6px 16px;
    }

    </style>
    """, unsafe_allow_html=True)