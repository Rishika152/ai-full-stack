from ollama import chat 

bad = "tell me about flowers."
good = "List 5 flowers that are suitable for closed environment. 2 lines each"

responseB = chat(
    model="llama3.2",
    messages=[{
        "role": "user",
        "content": bad
    }]
)

responseG = chat(
    model="llama3.2",
    messages=[{
        "role": "user",
        "content": good
    }]
)

print("Bad prompt response:", responseB["message"]["content"])
print("Good prompt response:", responseG["message"]["content"])
