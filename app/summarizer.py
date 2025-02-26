import openai
import re
import time
import logging
from config import API_KEY, MODEL_NAME
from logging_config import logger

class MedicalTextSummarizer:
    def __init__(self):
        if not API_KEY:
            raise ValueError("API key is missing. Set OPENAI_API_KEY in your environment.")
        self.api_key = API_KEY

    def summarize(self, text: str, mode: str = "brief"):
        if not text:
            raise ValueError("Invalid input: Text must be a non-empty string.")

        logger.info(f"Processing summary request - Mode: {mode}, Input Length: {len(text)} chars")
        start_time = time.time()

        if mode == "brief":
            prompt = f"Summarize the following medical note very concisely: {text}"
        elif mode == "json":
            prompt = (
                "Make sure to ONLY return the JSON format results and DO NOT INCLUDE '''json and '''.\n"
                "Important note: never make up or generate random results if you are not sure.\n"
                "critical_conditions should list the conditions separated by commas.\n"
                "general_summary should be an extremely concise summary of the notes.\n"
                "Format:\n"
                "{\n"
                '"patient_name": "",\n'
                '"age": "",\n'
                '"date_of_visit": "",\n'
                '"critical_conditions": "",\n'
                '"general_summary": "",\n'
                '"discharge_notes": ""\n'
                "}\n"
                f"Extract these details from the following medical note:\n{text}"
            )
        else:
            logger.error("Invalid mode selection.")
            raise ValueError("Invalid mode. Choose either 'brief' or 'json'.")

        try:
            response = openai.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a medical assistant."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=300
            )
            output = response.choices[0].message.content.strip()
            elapsed_time = time.time() - start_time

            input_tokens = response.usage.prompt_tokens if hasattr(response.usage, 'prompt_tokens') else 'N/A'
            output_tokens = response.usage.completion_tokens if hasattr(response.usage, 'completion_tokens') else 'N/A'

            logger.info(f"Summary generated in {elapsed_time:.2f}s | Input Tokens: {input_tokens}, Output Tokens: {output_tokens}")
            logger.debug(f"Summarized Output: {output}")

            if mode == "json":
                return self._parse_json_output(output)
            return output

        except Exception as e:
            logger.error(f"Summarization failed: {e}")
            raise

    def _parse_json_output(self, output: str):
        """Attempts to parse structured JSON output from the LLM."""
        import json
        try:
            return json.loads(output)
        except json.JSONDecodeError:
            logger.error("Failed to parse JSON response.")
            return {"error": "Failed to parse JSON response. Check format."}
