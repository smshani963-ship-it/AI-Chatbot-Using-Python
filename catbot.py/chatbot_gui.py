import tkinter as tk

def send(event=None):
    user = entry.get().lower()

    if user == "hello":
        reply = "Hello! How are you? "
    elif user == "hi":
        reply = "Hi! Nice to meet you! "
    elif user == "how are you":
        reply = "I'm doing great! "
    elif user == "bye":
        reply = "Goodbye! Have a nice day! "
    else:
        reply = "Sorry, I don't understand."
    chat.insert(tk.END, " You: " + user + "\n")
    chat.insert(tk.END, " Bot: " + reply + "\n\n")

    entry.delete(0, tk.END)

def clear_chat():
    chat.delete("1.0", tk.END)

window = tk.Tk()
window.title("AI Chatbot")
window.geometry("450x550")

chat = tk.Text(window, height=20, width=50, bg="white")
chat.pack(pady=10)

entry = tk.Entry(window, width=35)
entry.pack(pady=5)

entry.bind("<Return>", send)

send_button = tk.Button(window, text="Send", command=send)
send_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear Chat", command=clear_chat)
clear_button.pack()

window.mainloop()