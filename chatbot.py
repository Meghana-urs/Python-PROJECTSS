def get_bot_response(user_input):
    """
    Takes user input, normalizes it to lowercase, 
    and returns a predefined response using if-elif-else logic.
    """
    # Normalize input to make matching flexible (handles "Hello", "HELLO", etc.)
    user_input = user_input.lower().strip()
    
    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you today?"
    elif user_input == "how are you":
        return "I'm fine, thanks! How are you doing?"
    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. I am a simple bot!"

def start_chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit the conversation.")
    
    # Loop continuously to keep the conversation going
    while True:
        # Get input from the user
        user_message = input("You: ")
        
        # Get the appropriate response from our function
        bot_message = get_bot_response(user_message)
        
        # Output the bot's response
        print(f"Chatbot: {bot_message}")
        
        # Break the loop if the user wants to say goodbye
        if user_message.lower().strip() in ["bye", "goodbye"]:
            break

# Run the chatbot application
if __name__ == "__main__":
    start_chatbot()