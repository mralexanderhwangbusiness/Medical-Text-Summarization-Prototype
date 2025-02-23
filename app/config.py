import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
API_KEY = os.getenv("OPENAI_API_KEY")

# Define the model to use
MODEL_NAME = "gpt-4o"

# Ensure API key is properly loaded
if not API_KEY:
    raise ValueError("API key is missing. Set OPENAI_API_KEY in the .env file.")
