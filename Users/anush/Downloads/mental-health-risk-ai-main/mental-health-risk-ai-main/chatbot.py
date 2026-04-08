import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
print("Loaded API key:", API_KEY)

print("API KEY:", API_KEY)

def chat_response(message, history, chat_history):

    messages = []

    messages.append({
        "role": "system",
        "content": (
            "You are a supportive mental health assistant. "
            "Keep replies SHORT (1–2 sentences). "
            "Be empathetic and conversational. "
            "Suggest helpful coping strategies when needed."
        )
    })

    if history:
        messages.append({
            "role": "system",
            "content": f"User journal context: {history}"
        })

    for msg in chat_history[-6:]:
        messages.append(msg)

    messages.append({
        "role": "user",
        "content": message
    })

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": messages,
                "max_tokens": 80
            }
        )

        data = response.json()

        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]

        print("API response error:", data)

    except Exception as e:
        print("Chatbot error:", e)

    return "I'm here to listen. Tell me more."