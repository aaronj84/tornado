import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# print("let's do this")

# response.output_text = "chicken face"
# response = client.responses.create(
    # model="gpt-4o",
    # instructions="You are a coding assistant that talks like a pirate.",
    # input="How do I check if a Python object is an instance of a class?",
# )

def chat_with_gpt(prompt):
    try:
        # Send a request to ChatGPT
        response = client.responses.create(
            model="gpt-4o",
            # instructions="You are a coding assistant that talks like a pirate.",
            input=prompt,
        )

        return response.output_text
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    user_prompt = "Testing the API: Write a dark-humor haiku about chatgpt api interactions"
    response = chat_with_gpt(user_prompt)
    print("ChatGPT Response:", response)