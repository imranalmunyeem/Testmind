import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load API Key securely
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Use a .env file or set manually

# Check if API key is set
if not GEMINI_API_KEY:
    st.error("Google Gemini API key is missing! Set it as an environment variable or in a .env file.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Use the correct working model
MODEL_TO_USE = "gemini-1.5-pro-latest"  # Best available model

# Streamlit UI
st.set_page_config(page_title="TestMind - AI Test Automation", layout="wide")
st.title("🤖 TestMind: AI-Powered Test Case Generator")

st.markdown("### 🚀 Generate Automated & Manual Test Cases with AI")
st.write(
    "This tool uses **Google Gemini AI** to generate test cases for web automation frameworks or manual testing."
    " Simply provide your input, and TestMind will generate structured test cases."
)

# User Input Section
st.sidebar.header("🛠️ Test Case Configuration")

input_type = st.sidebar.selectbox(
    "🔍 What are you testing?",
    ["DOM Elements", "Raw Text Content", "Code Snippet"],
    help="Choose the type of input that AI should analyze for generating test cases.",
)

user_input = st.text_area(
    "✍️ Enter Test Content Below:",
    placeholder="Paste your HTML DOM, raw text, or code snippet...",
    height=150
)

test_type = st.sidebar.radio(
    "📝 Select Test Case Type:",
    ["Automated Test Cases", "Manual Test Cases"],
    help="Choose whether to generate test cases for automation frameworks or manual testing.",
)

test_framework = None
if test_type == "Automated Test Cases":
    test_framework = st.sidebar.selectbox(
        "🛠️ Select Automation Framework:",
        ["Cypress (JavaScript)", "Selenium (Python)", "Playwright (JavaScript)", "Postman (API Testing)"],
        help="Choose the test automation framework for which test cases should be generated.",
    )

execution_mode = None
if test_type == "Automated Test Cases":
    execution_mode = st.sidebar.radio(
        "🎯 What Do You Want to Do?",
        ["Generate Test Cases", "Generate & Execute Tests"],
        help="Choose whether to just generate test cases or also execute them.",
    )

debug_mode = st.sidebar.checkbox("🛠 Show Debug Info", help="Enable this to see API responses and errors.")

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

        # Call Google Gemini API
        try:
            model = genai.GenerativeModel(MODEL_TO_USE)
            response = model.generate_content(prompt)
            test_cases = response.text if hasattr(response, "text") else str(response)  # Extract response

            # Display AI-Generated Test Cases
            st.subheader("✅ AI-Generated Test Cases")

            # Use expandable section for better UI
            with st.expander("📜 Click to Expand Test Cases", expanded=True):
                st.code(test_cases, language="markdown")  # Code block format for better readability

            # Copy to Clipboard Button
            st.button("📋 Copy Test Cases", on_click=lambda: st.session_state.update({"copy": test_cases}))
            if "copy" in st.session_state:
                st.toast("✅ Test Cases Copied!")

            if test_type == "Automated Test Cases" and execution_mode == "Generate & Execute Tests":
                st.warning("🚀 Test Execution Feature Coming Soon!")

            # Debug Mode
            if debug_mode:
                st.subheader("🛠 Debugging Info")
                st.write(response)

        except Exception as e:
            st.error(f"⚠️ Google Gemini API Error: {e}")

    else:
        st.warning("⚠️ Please enter input data to generate test cases.")
