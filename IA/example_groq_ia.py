import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("API_KEY_GROQ"),
)

def ask_chat_groq(question: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama3-8b-8192",
    )

    return (chat_completion.choices[0].message.content)

##
question = "Onde fica o Brasil?"
result = ask_chat_groq(question)
print(result)
