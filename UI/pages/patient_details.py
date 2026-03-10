import streamlit as st
from services.patients import get_patient
from components.navbar import render_navbar

render_navbar()

patient_id = st.session_state.get("patient_id")

if patient_id is None:
    st.error("No patient selected")
    st.stop()

patient = get_patient(patient_id)[0]

col1, col2 = st.columns([1,6])

with col1:
    st.image(patient["profile_pic_url"], width=120)

with col2:
    st.title(f"{patient['first_name']} {patient['last_name']}")
    st.caption(f"DOB: {patient['date_of_birth']}")

st.divider()

tab1, tab2, tab3 = st.tabs(["Timeline", "Documents", "Summary"])

with tab1:
    st.subheader("Timeline")
    st.write("Document upload events")

with tab2:
    st.subheader("Documents")
    st.write("Document table")

with tab3:
    st.subheader("Summary")
    st.write("Auto summary of documents")