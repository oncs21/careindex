import streamlit as st
from services.patients import get_patient, get_patient_docs

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.style import apply_styles

apply_styles()
render_navbar()
render_sidebar()

patient_id = st.session_state.get("patient_id")

if patient_id is None:
    st.error("No patient selected")
    st.stop()

patient = get_patient(patient_id)[0]
docs = get_patient_docs(patient_id)

st.markdown('<div class="patient-header">', unsafe_allow_html=True)

col1, col2 = st.columns([1,6])

with col1:
    st.image(patient["profile_pic_url"], width=110)

with col2:
    st.markdown(f"## {patient['first_name']} {patient['last_name']}")
    st.caption(f"DOB: {patient['date_of_birth']}")

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

tab1, tab2, tab3 = st.tabs(["Timeline", "Documents", "Summary"])

with tab1:
    st.subheader("Timeline")


with tab2:
    st.subheader("Documents")
    
    if not docs:
        st.write("No documents found.")
    else:
        for doc in docs:
            st.write(f"{doc['title']}.{doc['file_ext']}")

with tab3:
    st.subheader("Summary")
    st.write("Auto summary of documents")