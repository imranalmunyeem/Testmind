import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key from .env or environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Validate API Key
if not GEMINI_API_KEY:
    raise ValueError("❌ Google Gemini API key is missing! Set it in a .env file or as an environment variable.")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Define the AI model to use
MODEL_TO_USE = "gemini-1.5-pro-latest"
