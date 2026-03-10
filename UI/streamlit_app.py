import streamlit as st
from components.navbar import render_navbar
from components.tiles import dashboard_tiles

st.set_page_config(
    page_title="CareIndex",
    page_icon="🩺",
    layout="wide"
)

render_navbar()

with st.sidebar:
    st.header("CareIndex")

    st.page_link("streamlit_app.py", label="Dashboard")
    st.page_link("pages/patients.py", label="Patients")
    st.page_link("pages/search.py", label="Search")
    st.page_link("pages/uploads.py", label="Uploads")

st.title("CareIndex")
st.caption("Clinic-scale document indexing and retrieval UI")

dashboard_tiles()