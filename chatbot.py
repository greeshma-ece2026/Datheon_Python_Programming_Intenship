import json
import re
import os

def load_faq():
    filename = "sample_faq-1.json"

    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read FAQ dataset.")

    return {}

def chatbot_response(message, faq_data):
    message = message.lower().strip()

    if re.search(r"\b(bye|exit|quit)\b", message):
        return "Goodbye! Thank you for chatting with us!"

    if re.search(r"\b(hi|hello|hey)\b", message):
        return "Hello! Welcome to our customer support assistant."

    responses = []

    if re.search(r"\b(hours|open|close|timing|time)\b", message):
        responses.append(
            "Our business hours are Monday to Saturday, 9 AM to 6 PM."
        )

    if re.search(r"\b(return|refund|exchange|replace)\b", message):
        responses.append(
            "Items can be returned within 7 days with the original receipt. "
            "Contact customer support to request a return."
        )

    if re.search(r"\b(product|price|available|delivery|shipping|warranty)\b", message):
        responses.append(
            "For product prices, availability, delivery, and warranty "
            "details, please check the product information or contact support."
        )

    # Search simple FAQ data for matching keywords
    if isinstance(faq_data, dict):
        for key, value in faq_data.items():
            if isinstance(key, str) and key.lower() in message:
                responses.append(str(value))

    if responses:
        return "\n".join(responses)

    return (
        "Sorry, I didn't understand that question. "
        "Please ask about business hours, products, or returns."
    )

def main():
    faq_data = load_faq()

    print("=" * 45)
    print("   CUSTOMER SUPPORT CHATBOT")
    print("=" * 45)
    print("Ask about business hours, products, or returns.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.")

    while True:
        try:
            user_message = input("\nYou: ").strip()

            if not user_message:
                print("Bot: Please enter a question.")
                continue

            response = chatbot_response(user_message, faq_data)
            print("Bot:", response)

            if re.search(r"\b(bye|exit|quit)\b", user_message.lower()):
                break

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break

if __name__ == "__main__":
    main()