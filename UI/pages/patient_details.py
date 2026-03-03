import streamlit as st

def get_patient_details(patient_id):
    return [
        {
            'id': 1,
            'f_name': 'John',
            'l_name': 'Doe',
            'age': 27,
            'profile_img': 'https://capecoraltech.edu/wp-content/uploads/2016/01/tutor-8-3.jpg'
        },
    ]

patient_id = st.session_state.get("patient_id", None)

if patient_id is None:
    st.error("No patient selected")
    st.stop()

try:
    patient_id = int(patient_id)
except ValueError:
    st.error(f"Patient ID must be an integer, currently it is {patient_id}")
    st.stop()

patient = get_patient_details(patient_id)
st.title(f"{patient[0]['f_name']} {patient[0]['l_name']}")