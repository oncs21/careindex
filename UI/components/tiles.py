import streamlit as st

def tile(title, description, page):

    st.markdown(f"""
    <a href="/{page}" target="_self" style="text-decoration:none;">
        <div class="card">
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
    </a>
    """, unsafe_allow_html=True)


def dashboard_tiles():

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        tile("Patients", "Manage patient vaults", "patients")

    with col2:
        tile("Vault", "Browse document categories", "search")

    with col3:
        tile("Search", "Smart document search", "search")

    with col4:
        tile("Uploads / Jobs", "Processing pipeline status", "uploads")