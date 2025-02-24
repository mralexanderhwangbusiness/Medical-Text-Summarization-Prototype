import openai
import re
from config import API_KEY, MODEL_NAME

class MedicalTextSummarizer:
    def __init__(self):
        if not API_KEY:
            raise ValueError("API key is missing. Set OPENAI_API_KEY in your environment.")
        self.api_key = API_KEY

    def summarize(self, text: str, mode: str = "brief"):
        if not text:
            raise ValueError("Invalid input: Text must be a non-empty string.")

        if mode == "brief":
            prompt = f"Summarize the following medical note very concisely: {text}"
        elif mode == "json":
            prompt = (
                "Extract the following details from the medical note. Return the output as a JSON object, but do not include '''json '''. Ensure correct JSON format with the following keys: Patient Name, Age, Date of Visit, Critical Conditions, and General Summary. If any key cannot be found, just fill it with an NA"
                f"\nMedical Note:\n{text}"
            )
        else:
            raise ValueError("Invalid mode. Choose either 'brief' or 'json'.")

        response = openai.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a medical assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=300
        )
        
        output = response.choices[0].message.content.strip()
        print(output)
        
        if mode == "json":
            return self._parse_json_output(output)
        return output

    def _parse_json_output(self, output: str):
        """Attempts to parse structured JSON output from the LLM."""
        import json
        try:
            return json.loads(output)
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON response. Check format."}
