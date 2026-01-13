import os
from pathlib import Path
from google import genai
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

        self.client = genai.Client(api_key=api_key)

    def send_prompt(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Gemini API Error: {str(e)}"
