def route_intent(user_message):
    message_lower = user_message.lower()
    
    # Simple keyword-based routing
    if "order" in message_lower or "status" in message_lower or "where" in message_lower:
        return {"intent": "order_status", "response": "[Placeholder] Order status lookup is not yet implemented. (Meshack's task)"}
    elif "return" in message_lower or "refund" in message_lower:
        return {"intent": "returns", "response": "[Placeholder] Returns logic is not yet implemented. (Meshack's task)"}
    else:
        # Task 11: Fallback message for unmatched questions (Victor's task)
        return get_fallback_message()

def get_fallback_message():
    return {
        "intent": "unmatched",
        "response": "I'm sorry, I can only help with checking Order Status and processing Returns right now. Let me connect you with a human support agent who can help you with your specific issue."
    }
