from ollama import chat
system_msg = "You are a poet. Answer in poetspeak. Answer in one sentence."
print("WELCOME TO ASTHRA CHATBOT 😊")
history = [{"role" : "system","content" : system_msg}]
question_counter = 0


while True:

    question = input("you:")
    if question == "":
        print("Asthra 🤖: please type something.")
        continue

    if question.lower().strip() == "/history":
        print("------ Your Conversation so far ------")
        if len (history) < 2 :
            print("Nothing here so far!")
        for msg in history[1:]:
            if msg["role"] == "user":
                speaker = "You"
            else:
                speaker = "Asthra 🤖"
            print(f"{speaker}: {msg["content"]}")
        print("-------------------------")
        print()
        continue
    
    if question.lower().strip() == "/clear":
        history = [{"role" : "system","content" : system_msg}]
        print("Your history is cleared. start a fresh conversation.")
        print()
        continue
    
    if question.lower().strip() == "/help":
        print("------ Available commands --------")
        print("/history - display conversation history")
        print("/clear - clear chat history")
        print("/help - display this list")
        print("exit = quits the chatbot")
        print("-----------------------------")
        print()
        continue
    
    
    if question.lower().strip() == "/personality": 
        new_personality = input("Enter new personality:")
        system_msg = new_personality
        history = [{"role" : "system","content" : system_msg}]
        print("You have sucessfully changes the personality")
        print()
        continue
    

   
    if question.lower().strip() in ["exit", "stop", "bye"]:
        print("Asthra 🤖: That's it for Today. please come back soon!👋👋")
        print(f"You asked {question_counter} today....")
        print()
        break
    history.append({"role" : "user","content" : question})
    question_counter += 1
    try:

        response = chat(
            model = "llama3.2",
            messages= history
        )
        reply = response.message.content
        history.append({"role" : "assiatant", "content" :"reply"})
        print(f"Asthra 🤖: {response.message.content}")
        print("------------------------------------")

    except Exception as e:
        print("Unknown issue. Isollama running?")