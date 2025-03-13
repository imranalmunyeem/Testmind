import streamlit as st
from ai_handler import generate_test_cases
from ui_components import sidebar_options, display_results

# Streamlit UI Setup
st.set_page_config(page_title="TestMind - AI Test Automation", layout="wide")
st.title("🤖 TestMind: AI-Powered Test Case Generator")

st.markdown("### 🚀 Generate Automated & Manual Test Cases with AI")
st.write(
    "This tool uses **Google Gemini AI** to generate test cases for web automation frameworks or manual testing."
    " Simply provide your input, and TestMind will generate structured test cases."
)

# Sidebar Options
input_type, test_type, test_framework, execution_mode, debug_mode = sidebar_options()

# User Input Section
user_input = st.text_area(
    "✍️ Enter Test Content Below:",
    placeholder="Paste your HTML DOM, raw text, or code snippet...",
    height=150
)

# Generate Test Cases Button
if st.button("✨ Generate AI Test Cases"):
    if user_input:
        # AI Prompt
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

        # Call AI Handler to Generate Test Cases
        test_cases = generate_test_cases(prompt)

        # Display Results
        display_results(test_cases)

    else:
        st.warning("⚠️ Please enter input data to generate test cases.")
