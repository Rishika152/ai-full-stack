from ollama import chat 
prompt = "I'm late to class"

for t in [0, 0.5, 5]:
    print(f"Temp; {t}")
    for run in range(3):
        response = chat(
           model = "llama3.2",
                messages=[
                    {
                        "role" : "user",
                        "content" : prompt
                    }
                ],
                options = {"temperature" : t}
            )
        print(f"Run {run + 1}: {response.message.content}")
    print()