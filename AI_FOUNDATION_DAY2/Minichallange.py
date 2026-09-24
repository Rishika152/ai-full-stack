from ollama import chat

response = chat(
    model = "llama3.2",

    messages = [
        {"role": "system", "content": "Think that you are a mood based reply chat botalways give me reply in this format: /nsong gener:.../nsnacks:..../nactivity.."},

        {"role": "user", "content": "MOOD: Happy"},
        {"role": "assistant", "content": "/nsong genre pop/nancks chips/nActivity Dancing"},

        {"role": "user", "content": "MOOD: Sad"},
        {"role": "assistant", "content": "/nsong genre sad/n snacks icecream/nActivity Drawing"},

        {"role": "user", "content": "MOOD: Energetic"},
        {"role": "assistant", "content": "/nsong genre jazz/nsnacks Home food/nActivity Singing"},

        {"role": "user", "content":"MOOD: Enthusisastic"}
        ],
        options = {"temperature": 1.5}
    )
print(response["message"]["content"])
