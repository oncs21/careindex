import streamlit as st

from components.navbar import render_navbar
from components.tiles import dashboard_tiles
from components.style import apply_styles
from components.sidebar import render_sidebar

st.set_page_config(
    page_title="CareIndex",
    page_icon="🩺",
    layout="wide"
)

apply_styles()

render_navbar()
render_sidebar()

dashboard_tiles()