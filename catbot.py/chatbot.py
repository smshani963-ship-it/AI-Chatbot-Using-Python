import datetime
import random
print(" AI Chatbot")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you?")
    elif user == "hi":
        print("Bot: Hi! Nice to meet you.")
    elif user == "how are you":
        print("Bot: I'm doing great. How about you?")
    elif user == "fine":
        print("Bot: That's great to hear!")
    elif user == "good":
        print("Bot: Nice! Keep smiling. ")
    elif user == "your name":
        print("Bot: My name is AI Chatbot.")
    elif user == "what can you do":
        print("Bot: I can chat with you and answer simple questions.")
    elif user == "thank you":
        print("Bot: You're welcome! ")
    elif user == "who created you":
        print("Bot: Shani created me as a Python project.")

    elif user == "time":
         now = datetime.datetime.now()
         print("Bot: Current time is", 
    now.strftime("%I:%M %p"))

    elif user == "joke":
         jokes = [
        "Why did the computer go to the doctor? Because it had a virus!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the keyboard break up with the mouse? It got clicked too much!"
        ]
         print("Bot:", random.choice(jokes))

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that yet.")