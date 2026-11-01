
def chatbot_response(message):
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hello! How can I help you?"

    elif message == "how are you":
        return "I am fine, thank you!"

    elif message == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that message."


def main():
    print("===== Basic Python Chatbot =====")
    print("Type 'hello', 'how are you', or 'bye'.")

    while True:
        user_message = input("You: ")
        response = chatbot_response(user_message)

        print("Chatbot:", response)

        if user_message.lower().strip() == "bye":
            break


main()
