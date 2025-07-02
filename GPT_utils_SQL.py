import requests
import os
from config import api_key

# Secure API Key Handling
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ ERROR: Set your OpenAI API key as environment variable 'OPENAI_API_KEY'")
    exit()

def get_summary(text):
    """
    Uses GPT to summarize SQL query results into simple, human-friendly insights.
    """
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You summarize SQL query results for easy understanding."},
            {"role": "user", "content": f"Summarize this SQL result:\n{text}"}
        ],
        "max_tokens": 150
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"❌ AI Error: {e}")
        return "⚠️ AI could not generate summary."
