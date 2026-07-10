from transformers import pipeline
import torch
from config import SYSTEM_PROMPT

print("Loading Deek AI...")

chat = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct",
    torch_dtype=torch.float16,
    device_map="auto"
)

print("Deek AI Loaded!")

def ask(user_message):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    response = chat(
        messages,
        max_new_tokens=200,
        do_sample=False
    )

    return response[0]["generated_text"][-1]["content"]
