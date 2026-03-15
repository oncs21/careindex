import streamlit as st

def render_navbar():

    col1, col2, col3 = st.columns([2,5,2])

    with col1:
        st.markdown("### 🩺 CareIndex")

    with col2:
        st.markdown(
        """
        <div style="padding-top:10px">

        <a href="/" style="margin-right:20px;text-decoration:none;">Dashboard</a>
        <a href="/patients" style="margin-right:20px;text-decoration:none;">Patients</a>
        <a href="/search" style="margin-right:20px;text-decoration:none;">Search</a>
        <a href="/uploads" style="text-decoration:none;">Uploads</a>

        </div>
        """,
        unsafe_allow_html=True
        )

    with col3:
        st.markdown(
        "<div style='text-align:right;padding-top:10px'>Dr. User</div>",
        unsafe_allow_html=True
        )

    st.text_input(
        "",
        placeholder="Search patients, documents...",
        key="global_search",
        label_visibility="collapsed"
    )

    st.divider()