import streamlit as st
from services.patients import get_patient

patient_id = st.session_state.get("patient_id", None)

if patient_id is None:
    st.error("No patient selected")
    st.stop()

try:
    patient_id = int(patient_id)
except ValueError:
    st.error(f"Patient ID must be an integer, currently it is {patient_id}")
    st.stop()

patient = get_patient(patient_id)[0]
st.title(f"{patient['first_name']} {patient['last_name']}")

st.write(f"DOB = {patient["date_of_birth"]}")

st.write("# Timeline")
st.write("# Documents")
st.write("# Summary")