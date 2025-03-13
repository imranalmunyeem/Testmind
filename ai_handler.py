import google.generativeai as genai
from config import MODEL_TO_USE

def generate_test_cases(prompt):
    """ Calls Google Gemini API and returns generated test cases. """
    try:
        model = genai.GenerativeModel(MODEL_TO_USE)
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else str(response)  # Extract AI response
    except Exception as e:
        return f"⚠️ AI Error: {e}"
