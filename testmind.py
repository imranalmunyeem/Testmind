import streamlit as st
from ai_handler import generate_test_cases
from ui_components import sidebar_options, display_results
from utils import export_test_cases, toggle_theme

# ---- Streamlit UI Customization ----
st.set_page_config(
    page_title="TestMind - AI Test Automation",
    layout="wide",
    page_icon="🧪"
)

# ---- Dark Mode Toggle ----
toggle_theme()

# ---- Header with Logo & Description ----
col1, col2 = st.columns([0.2, 0.8])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039525.png", width=100)  # TestMind Logo
with col2:
    st.title("🚀 TestMind: AI-Powered Test Automation")
    st.markdown(
        "### ✅ AI-powered test generation for **automation & manual testing**"
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
            - Suggest missing test cases for better coverage.
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
            - **Suggest improvements for better test coverage.**
            """

        # ---- Call AI Handler ----
        test_cases = generate_test_cases(prompt)

        # Update progress bar
        progress_bar.progress(100)
        st.success("✅ AI Test Cases Generated Successfully!")

        # ---- Display Results ----
        display_results(test_cases)

        # ---- Export Options ----
        export_test_cases(test_cases)

    else:
        st.warning("⚠️ Please enter input data to generate test cases.")
