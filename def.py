RESPONSES = {
    "exact": {
        ("hello", "hi"): "Hello! How can I assist you today?",
        ("bye",): "Goodbye! Have a great day!",
    },
    "keyword": {
        "name": "My name is NaroBOt.",
        "python": "Python is a popular programming language known for its simplicity and versatility.",
        "college": "I am a Virtual Assistant.",
        "help": "Sure! I can help you with various tasks. What do you need assistance with?",
        "what help u need": "Sure! tell me I am ur assistant ",
    }
}

DEFAULT_RESPONSE = "I'm sorry, I didn't understand that. Can you please rephrase your question?"


def chatbot_response(user_input):
    """Generate a response based on user input."""
    user_input_lower = user_input.lower().strip()
    
    # Check exact matches
    for triggers, response in RESPONSES["exact"].items():
        if user_input_lower in triggers:
            return response
    
    # Check keyword matches
    for keyword, response in RESPONSES["keyword"].items():
        if keyword in user_input_lower:
            return response
    
    return DEFAULT_RESPONSE


def main():
    """Run the chatbot in interactive mode."""
    print("🤖 AI Chatbot Started!")
    print("   Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        if user_input:  # Ignore empty inputs
            response = chatbot_response(user_input)
            print(f"Chatbot: {response}\n")


if __name__ == "__main__":
    main()