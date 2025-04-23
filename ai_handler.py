import google.generativeai as genai
from config import MODEL_TO_USE

def generate_test_cases(prompt):
    """
    Generate test cases using Google Gemini API based on the input prompt.

    Returns AI-generated test cases as a string (Markdown or structured text).
    """
    try:
        # Initialize the Generative Model
        model = genai.GenerativeModel(model_name=MODEL_TO_USE)

        # Generate response
        response = model.generate_content(prompt)

        # Return formatted output
        if hasattr(response, "text"):
            return response.text.strip()
        elif hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].text.strip()
        else:
            return "⚠️ No response received from AI."

    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"
