import streamlit as st

def render_sidebar():

    with st.sidebar:

        st.markdown("## 🩺 CareIndex")
        st.caption("Clinic document system")

        st.divider()

        st.page_link("streamlit_app.py", label="Dashboard")
        st.page_link("pages/patients.py", label="Patients")
        st.page_link("pages/search.py", label="Search")
        st.page_link("pages/uploads.py", label="Uploads")