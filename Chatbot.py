import random

# Dictionary to hold predefined responses
responses = {
    "hello": "Hello! How can I help you today?",
    "how are you": "I'm just a computer program, but I'm functioning well. How about you?",
    "goodbye": "Goodbye! Have a great day.",
    "default": "I'm sorry, I don't understand. Can you rephrase or ask something else?"
}

def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user's input matches a predefined response
    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]

def main():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day.")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
