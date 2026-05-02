import os 
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {"role": "system", "content": "Ты полезный помощник"}
]

while True:
    user_input = input("Ты: ")

    if user_input == "выход":
        break 
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model = 'llama-3.1-8b-instant',
        messages = messages
    )  

    answer = response.choices[0].message.content

    messages.append({"role": "assistant", "content": answer})

    print("агент: ", answer)