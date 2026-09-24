from ollama import chat 

messages = [
    {"role": "system", "content": "Identify sentiment as positive, negative, neutral. Reply with one word only."},

    {"role": "user", "content": "Great Movie."},
    {"role": "assistant", "content": "positive"},

    {"role": "user", "content": "Waste of money"},
    {"role": "assistant", "content": "negative"},

    {"role": "user", "content": "It was okay."},
    {"role": "assistant", "content": "neutral"},

    {"role": "user", "content": "Loved the acting but the ending was dull"}
]

response = chat(
    model="llama3.2",
    messages=messages
)

print(response.message.content)
