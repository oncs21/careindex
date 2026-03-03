import streamlit as st
from PIL import Image

def get_patients():
    return [
        {
            'id': 1,
            'f_name': 'John',
            'l_name': 'Doe',
            'age': 27,
            'profile_img': 'https://capecoraltech.edu/wp-content/uploads/2016/01/tutor-8-3.jpg'
        },
        {
            'id': 2,
            'f_name': 'Carlos',
            'l_name': 'Alcaraz',
            'age': 47,
            'profile_img': 'https://a.espncdn.com/combiner/i?img=/i/headshots/tennis/players/full/3782.png'
        }
    ]

st.title("Patients")

patients = get_patients()

for patient in patients:
    col1, col2, col3 = st.columns([1, 4, 1], vertical_alignment='center')

    with col1:
        st.image(patient['profile_img'], width=60)

    with col2:
        st.markdown(
            f"""
            <div style="display:flex; align-items:center; height:60px;">
                <span style="font-size:18px;">
                    {patient['f_name']} {patient['l_name']}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        if st.button("View", key=f"view_{patient['id']}"):
            st.session_state["patient_id"] = str(patient["id"])
            st.switch_page(f"pages/patient_details.py")
