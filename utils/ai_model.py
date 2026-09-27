import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-3.8-flash")

def get_ai_response(user_input):

    try:
        response = model.generate_content(user_input)
        return response.text

    except Exception as e:
        return f"Error: {e}"

    