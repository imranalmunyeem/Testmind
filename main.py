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

# ---- Theme Toggle ----
toggle_theme()

# ---- Header with Branding ----
col1, col2 = st.columns([0.2, 0.8])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3039/3039525.png", width=100)  # Logo
with col2:
    st.title("🚀 TestMind: AI-Powered Test Automation Framework")
    st.markdown(
        "### 🤖 Multi-framework test case generation for **automation & manual QA**"
        "\n> Powered by LLMs. Supports **Cypress**, **Selenium**, **Playwright**, **Postman**."
    )

# ---- Sidebar User Configurations ----
input_type, test_type, test_framework, execution_mode, debug_mode = sidebar_options()

# ---- Input Section ----
st.markdown("### ✍️ Provide Your Test Context")
user_input = st.text_area(
    "💡 Paste your DOM, endpoint, user scenario, or raw text:",
    placeholder="e.g. HTML element, /api/login, login form, or functional spec",
    height=150
)

# ---- Trigger Test Case Generation ----
if st.button("✨ Generate Test Cases", use_container_width=True):
    if user_input:
        progress_bar = st.progress(0)
        st.markdown("⏳ *Processing input with AI... Please wait.*")

        # ---- LLM Prompt Based on Inputs ----
        if test_type == "Automated Test Cases":
            prompt = f"""
            You are an AI QA engineer. Generate **{test_framework} automation test cases** for the input below.
            Input Type: **{input_type}**
            Framework: **{test_framework}**
            Test Content:
            ```
            {user_input}
            ```

            Instructions:
            - Follow best practices in automation design.
            - Include selectors, actions, and validations.
            - Add relevant assertions.
            - Ensure readability, modularity, and scalability.
            - Suggest edge or negative cases for enhanced coverage.
            """
        else:  # Manual Test Case Prompt
            prompt = f"""
            You are a senior QA analyst. Create structured **manual test cases** based on this input.
            Input Type: **{input_type}**
            Test Content:
            ```
            {user_input}
            ```

            Each test case must contain:
            - **Title / Scenario**
            - **Step-by-step instructions**
            - **Expected Result**
            - **Test Priority**
            - **Preconditions**
            - Optionally recommend additional cases.
            """

        # ---- Call AI Model Handler ----
        test_cases = generate_test_cases(prompt)

        progress_bar.progress(100)
        st.success("✅ Test Cases Generated Successfully!")

        # ---- Display & Export Output ----
        display_results(test_cases)
        export_test_cases(test_cases)

    else:
        st.warning("⚠️ Please provide input data to continue.")
