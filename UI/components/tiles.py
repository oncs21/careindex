import streamlit as st

def dashboard_tiles():

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Patients")
            st.caption("Manage patient vaults")
            if st.button("Open", key="patients_btn"):
                st.switch_page("pages/patients.py")

    with col2:
        with st.container(border=True):
            st.subheader("Vault")
            st.caption("Browse document categories")

    with col3:
        with st.container(border=True):
            st.subheader("Search")
            st.caption("Smart document search")

    with col4:
        with st.container(border=True):
            st.subheader("Uploads / Jobs")
            st.caption("Processing pipeline status")