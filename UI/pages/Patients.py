import streamlit as st
from services.patients import get_patients
from components.navbar import render_navbar
from components.patient_card import patient_card

render_navbar()

st.title("Patients")

patients = get_patients()

for patient in patients:
    patient_card(patient)