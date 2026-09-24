from ollama import chat

response = chat(
    model="llama3.2",
    messages=[{
        "role": "user",cd
        "content": "give me a road map for the ai full stack course"
    }]
)

print(response["message"]["content"])
