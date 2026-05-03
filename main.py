import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
API_URL = "https://api.openai.com/v1/responses"

def generate_code(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4.1-mini",
        "input": f"Write clean, well-commented code:\n{prompt}"
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["output"][0]["content"][0]["text"]
    else:
        return f"Error: {response.text}"


if __name__ == "__main__":
    print("=== AI Code Generator ===\n")

    while True:
        prompt = input("Enter what you want (or 'exit'): ")

        if prompt.lower() == "exit":
            break

        code = generate_code(prompt)

        print("\n--- Generated Code ---\n")
        print(code)
        print("\n----------------------\n")
