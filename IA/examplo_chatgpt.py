import openai
import os
from dotenv import load_dotenv

load_dotenv()

# api key
openai.api_key = os.getenv("API_KEY_OPENAI")

# function
def ask_chatgpt(question: str):
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"rule": "user", "content": ""}
        ]
    )

    # extract the actual content message
    return response.choices[0].message.content

# parameters
question = "Quantos anos o Brasil tem?"
answer = ask_chatgpt(question)

# print
print(f"Resposta do Chatgpt: {answer}")
