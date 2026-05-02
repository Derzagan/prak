import os 
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))    

message = [{"role": "system", "content": """Ты определяешь тональность текста.
Отвечай только одним словом: позитив, негатив, нейтрально.

Пример:
user: Сегодня отличный день!
assistant: позитив

Пример:
user: Всё ужасно и плохо
assistant: негатив

Пример:
user: Завтра будет дождь
assistant: нейтрально
"""},
    {"role": "user", "content": "мне все равно"     }
]

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=message


)

print(response.choices[0].message.content)