import openai
from app.config import API_KEY, MODEL_NAME

class MedicalTextSummarizer:
    def __init__(self):
        if not API_KEY:
            raise ValueError("API key is missing. Set OPENAI_API_KEY in your environment.")
        self.api_key = API_KEY

    def summarize(self, text: str) -> str:
        if not text:
            raise ValueError("Invalid input: Text must be a non-empty string.")

        prompt = f"Summarize the following medical note very concisely: {text}"

        response = openai.chat.completions.create(  # Updated method
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a medical assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=250
        )

        return response.choices[0].message.content.strip()
