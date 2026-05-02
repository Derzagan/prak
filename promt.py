import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": "Ты саркастичный помощник который отвечает с юмором и подколками"},
        {"role": "user", "content": "Привет! Что такое Python?"},
    ]
)

print(response.choices[0].message.content)