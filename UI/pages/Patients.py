import streamlit as st

from services.patients import get_patients

from components.navbar import render_navbar
from components.patient_card import patient_card
from components.sidebar import render_sidebar
from components.style import apply_styles

apply_styles()
render_navbar()
render_sidebar()

st.title("Patients")

patients = get_patients()

for patient in patients:
    patient_card(patient)