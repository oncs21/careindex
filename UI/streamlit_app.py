import streamlit as st

st.title("CareIndex")
st.caption("Clinic-scale document indexing and retrieval UI")

with st.sidebar:
    st.subheader("Workspace")

    st.text_input("API Base URL", key="api_base", help="Example")

col1, col2, col3 = st.columns([1.2, 1, 1])

with col1:
    st.markdown("### What you can do")
    st.markdown(
        """
- Create patients' document vault and manage them
- Upload documents and track processing jobs
- Search by keywords + filters
- View patient timeline and recent activity
""".strip()
    )

with col2:
    st.markdown("### Quick status")

with col3:
    st.markdown("### Checklist")

st.info("Use the left sidebar navigation for quick access.")