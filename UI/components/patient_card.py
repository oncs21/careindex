import streamlit as st

def patient_card(patient):
    col1, col2, col3 = st.columns([1,6,2])

    with col1:
        st.image(patient["profile_pic_url"], width=60)

    with col2:
        st.markdown(
            f"""
            **{patient['first_name']} {patient['last_name']}**

            DOB: {patient['date_of_birth']}
            """,
        )

    with col3:
        if st.button("Open", key=f"open_{patient['id']}"):
            st.session_state["patient_id"] = patient["id"]
            st.switch_page("pages/patient_details.py")

    st.divider()