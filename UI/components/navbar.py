import streamlit as st

def render_navbar():

    col1, col2, col3 = st.columns([3, 4, 2])

    with col1:
        st.markdown("### CareIndex")

    with col2:
        st.text_input(
            "Search documents, patients...",
            key="global_search",
            label_visibility="collapsed",
            placeholder="Search patients, documents..."
        )

    with col3:
        st.markdown(
        """
        <div style='text-align:right; padding-top:8px'>
        User
        </div>
        """,
        unsafe_allow_html=True
        )

    st.divider()