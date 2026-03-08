import streamlit as st
from services.patients import get_patients

st.title("Patients")

patients = get_patients()

for patient in patients:
    col1, col2, col3 = st.columns([1, 4, 1], vertical_alignment='center')

    with col1:
        st.image(patient['profile_pic_url'], width=60)

    with col2:
        st.markdown(
            f"""
            <div style="display:flex; align-items:center; height:60px;">
                <span style="font-size:18px;">
                    {patient['first_name']} {patient['last_name']}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        if st.button("View", key=f"view_{patient['id']}"):
            st.session_state["patient_id"] = str(patient["id"])
            st.switch_page(f"pages/patient_details.py")
