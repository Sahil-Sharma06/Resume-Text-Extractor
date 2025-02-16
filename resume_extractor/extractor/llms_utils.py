import requests
import os
from dotenv import load_dotenv

# Load API key from environment variables
load_dotenv()
LLAMA_API_KEY = os.getenv("LA-e787162c1a244df081c7807fefa88539a766fb2285454ea392186bc27234bdfe")
LLAMA_API_URL = "https://api.llama-api.com/chat/completions"  # Replace with your actual API endpoint

def get_structured_resume(text):
    prompt = f"""
    Extract and structure the following resume text into JSON format with keys:
    name, contact, education, experience, skills.

    Resume text:
    {text}
    """

    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-2-7b-chat",  # Adjust model name as per your API
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 500
    }

    response = requests.post(LLAMA_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return {"error": f"API Error {response.status_code}: {response.json()}"}
