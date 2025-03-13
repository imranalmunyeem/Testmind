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
st.title("TestMind: AI-Powered Test Case Generator (Google Gemini)")

# User Input
input_type = st.selectbox("Select Input Type:", ["DOM", "Raw Content", "Subject Line", "Code"])
user_input = st.text_area("Enter your input data:")

# Test Framework Selection
test_framework = st.selectbox("Select Test Framework:", ["Cypress", "Selenium", "Playwright", "Postman"])

# Generate Test Cases Button
if st.button("Generate Test Cases"):
    if user_input:
        # Gemini Prompt
        prompt = f"""
        Generate well-structured {test_framework} test cases for the following {input_type}:
        {user_input}
        Ensure the test cases follow best practices, include assertions, and are optimized for automation.
        """

        # Call Google Gemini API
        try:
            model = genai.GenerativeModel(MODEL_TO_USE)
            response = model.generate_content(prompt)

            test_cases = response.text if hasattr(response, "text") else str(response)  # Extract response
            st.text_area("Generated Test Cases:", test_cases, height=300)

        except Exception as e:
            st.error(f"Google Gemini API Error: {e}")

    else:
        st.warning("Please enter input data to generate test cases.")
