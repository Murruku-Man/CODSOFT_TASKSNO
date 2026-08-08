# CODSOFT Task 1 - Rule-Based Chatbot

from datetime import datetime


def chatbot_response(user_input):
    """Return a predefined response based on the user's input."""
    text = user_input.lower().strip()

    if not text:
        return "Please type something so I can respond."

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
        return "Hello! Nice to meet you. How can I help you?"

    # Name
    elif "your name" in text or "who are you" in text:
        return "I'm RuleBot, a simple rule-based chatbot created for the CodSoft AI internship."

    # Capabilities
    elif "what can you do" in text or "help" in text:
        return "I can respond to greetings, answer basic questions, tell you the date and time, and handle simple conversations using predefined rules."

    # How are you
    elif "how are you" in text:
        return "I'm doing great! Thanks for asking."

    # Date
    elif "date" in text or "today" in text:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."

    # Time
    elif "time" in text:
        return f"The current time is {datetime.now().strftime('%I:%M:%S %p')}."

    # Thanks
    elif any(word in text for word in ["thank you", "thanks", "thank"]):
        return "You're welcome! Glad I could help."

    # Goodbye
    elif any(word in text for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! Have a great day."

    # Default response
    else:
        return "Sorry, I don't understand that yet. Try asking about my name, capabilities, date, or time."


def main():
    print("=" * 55)
    print("             RULE-BASED CHATBOT")
    print("              CODSOFT - TASK 1")
    print("=" * 55)
    print("Chatbot: Hello! I'm RuleBot.")
    print("Chatbot: Type 'bye' or 'exit' to end the conversation.")
    print()

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()
