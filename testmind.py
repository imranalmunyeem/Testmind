import streamlit as st
from ai_handler import generate_test_cases
from ui_components import sidebar_options, display_results

# ---- Streamlit UI Customization ----
st.set_page_config(
    page_title="TestMind - AI Test Automation",
    layout="wide",
    page_icon="🧪"
)

# ---- Custom Styling for a Sleek Look ----
st.markdown(
    """
    <style>
        /* Global Styling */
        body { font-family: 'Arial', sans-serif; background-color: #f4f4f4; }
        .main { background-color: white; padding: 20px; border-radius: 10px; }
        .stTextArea textarea { font-size: 14px !important; }
        .stButton button { border-radius: 8px; background-color: #1f77b4; color: white; font-weight: bold; }
        .stButton button:hover { background-color: #105a8b; }
        .stSidebar { background-color: #1e1e1e !important; color: white !important; }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Header with Logo & Description ----
col1, col2 = st.columns([0.2, 0.8])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039525.png", width=100)  # TestMind Logo
with col2:
    st.title("🚀 TestMind: AI-Powered Test Automation")
    st.markdown(
        "### ✅ Generate industry-standard test cases for **automation & manual testing** using AI!"
        "\n> Supports **Cypress, Selenium, Playwright, Postman**, and more."
    )

# ---- Sidebar Options ----
input_type, test_type, test_framework, execution_mode, debug_mode = sidebar_options()

# ---- User Input Section ----
st.markdown("### ✍️ Enter Test Content")
user_input = st.text_area(
    "💡 Provide a snippet of HTML, text, or code to generate test cases.",
    placeholder="Paste your HTML DOM, raw text, or code snippet...",
    height=150
)

# ---- Generate Test Cases Button ----
if st.button("✨ Generate AI Test Cases", use_container_width=True):
    if user_input:
        # Show progress bar
        progress_bar = st.progress(0)
        st.markdown("⏳ *Generating test cases... Please wait...*")

        # ---- AI Prompt Construction ----
        if test_type == "Automated Test Cases":
            prompt = f"""
            Generate structured **{test_framework}** test cases based on the following **{input_type}**:
            ```
            {user_input}
            ```
            - Ensure best automation practices.
            - Include assertions for verification.
            - Optimize for maintainability and reusability.
            - Provide step-by-step instructions if necessary.
            """
        else:  # Manual Test Cases
            prompt = f"""
            Generate well-structured **manual test cases** for the following **{input_type}**:
            ```
            {user_input}
            ```
            Each test case should include:
            - **Test Scenario Name**
            - **Test Steps**
            - **Expected Result**
            - **Test Priority** (High, Medium, Low)
            - **Preconditions** (If applicable)
            """

        # ---- Call AI Handler ----
        test_cases = generate_test_cases(prompt)

        # Update progress bar
        progress_bar.progress(100)
        st.success("✅ AI Test Cases Generated Successfully!")

        # ---- Display Results ----
        display_results(test_cases)

    else:
        st.warning("⚠️ Please enter input data to generate test cases.")
