def chatbot():
    print("🤖 Hello! I'm ChatBot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there! How can I help you today?")
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Bot: I'm ChatBot, your friendly assistant!")
        elif "weather" in user_input:
            print("Bot: I can’t check the weather yet, but I hope it’s nice where you are!")
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {now}.")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day! 👋")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()