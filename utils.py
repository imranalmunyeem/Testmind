import streamlit as st

def export_test_cases(test_cases):
    """ Allows users to export test cases in different formats. """
    st.markdown("### 📂 Export Test Cases")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.download_button("📜 Export as TXT", test_cases, file_name="test_cases.txt")

    with col2:
        st.download_button("📂 Export as JSON", test_cases, file_name="test_cases.json")

    with col3:
        st.download_button("📊 Export as CSV", test_cases, file_name="test_cases.csv")

def toggle_theme():
    """ Adds a dark mode/light mode toggle for better UI experience. """
    dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode", help="Switch between dark and light themes.")
    
    if dark_mode:
        st.markdown("""
            <style>
                body { background-color: #1e1e1e; color: white; }
                .stSidebar { background-color: black !important; }
                .stButton button { background-color: #f39c12 !important; color: black !important; }
            </style>
        """, unsafe_allow_html=True)
