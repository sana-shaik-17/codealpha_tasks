def chatbot():

    print("===================================")
    print("      Welcome to Basic Chatbot")
    print("Type 'bye' to exit.")
    print("===================================")

    while True:

        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "hi":
            print("Bot: Hello!")

        elif user == "how are you":
            print("Bot: I'm fine, thank you!")

        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "what can you do":
            print("Bot: I can answer simple predefined questions.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Start Chatbot
chatbot()
