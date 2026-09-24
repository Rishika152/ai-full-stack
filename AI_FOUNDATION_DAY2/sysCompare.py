from ollama import chat

roles = [
    "you are a maths teacher. Answer briskly and within 3 lines",
    "you are a movie director. Answer in filmy way, one line only",
    "you are a lawyer. Answer professionally, one line only"
]

for role in roles:
    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": role
            },
            {
                "role": "user",
                "content": "Speak about virat kohli?"
            }
        ]
    )
    print(f"--- {role} ---")
    print(response["message"]["content"])
    print()
