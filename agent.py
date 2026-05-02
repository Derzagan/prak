import os
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def calculate(expression):
    result = eval(expression)
    return str(result)


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Считает математические выражения",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression":{
                        "type": "string",
                        "description": "Математическое выражение например 2+2"

                    }
                },
                "required": ["expression"]
            }
        }
    }
]


messages = [
    {"role": "system", "content": "Ты помощник. Для математики используй инструмент calculate"},
    {"role": "user", "content": "Сколько будет 25 умножить на 48?"}
]
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=messages,
    tools=tools
)

if response.choices[0].message.tool_calls:
    tools_call = response.choices[0].message.tool_calls[0]

    args = json.loads(tools_call.function.arguments)
    print("Модель вызвала инструмент", tools_call.function.name)
    print("С аргументом", args["expression"])

    result = calculate(args["expression"])
    print("Результат", result)



messages.append(response.choices[0].message)


messages.append({
    "role": "tool",
    "tool_call_id": tools_call.id,
    "content": result
})


final = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=messages,
    tools=tools
)


print("Агент:", final.choices[0].message.content)