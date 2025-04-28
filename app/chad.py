import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        # Send a request to ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        # Parse the response
        reply = response['choices'][0]['message']['content']
        return reply
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    user_prompt = "Hello, ChatGPT! How are you?"
    response = chat_with_gpt(user_prompt)
    print("ChatGPT Response:", response)