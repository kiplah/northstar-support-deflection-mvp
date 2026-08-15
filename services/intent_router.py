import re

from services.order_service import get_order_status
from services.returns_service import check_return_eligibility


def route_intent(user_message):
    message = user_message.strip()
    message_lower = message.lower()

    # -------------------------
    # ORDER STATUS
    # -------------------------

    order_match = re.search(
        r"\b(?:ord[-\s]?)?(\d{4})\b",
        message_lower
    )

    if (
        "order" in message_lower
        and (
            "status" in message_lower
            or "where" in message_lower
            or "track" in message_lower
        )
    ):
        if order_match:
            order_id = f"ORD-{order_match.group(1)}"
            result = get_order_status(order_id)

            return {
                "intent": "order_status",
                "response": result["message"]
            }

        return {
            "intent": "order_status",
            "response": (
                "Please provide your order ID, "
                "for example ORD-1001."
            )
        }

    # -------------------------
    # RETURNS
    # -------------------------

    if "return" in message_lower or "refund" in message_lower:

        categories = [
            "Electronics",
            "Accessories",
            "Home Goods",
            "Apparel",
            "Software",
            "Beauty"
        ]

        reasons = [
            "Defective",
            "Damaged in transit",
            "Wrong item",
            "Not as described",
            "Changed mind",
            "Wrong size",
            "Billing issue"
        ]

        category = None
        reason = None

        # Find category in the user's message
        for item in categories:
            if item.lower() in message_lower:
                category = item
                break

        # Find reason in the user's message
        for item in reasons:
            if item.lower() in message_lower:
                reason = item
                break

        if category and reason:
            result = check_return_eligibility(
                category,
                reason
            )

            return {
                "intent": "returns",
                "response": (
                    f"{result['message']} "
                    f"{result['next_step']}"
                )
            }

        return {
            "intent": "returns",
            "response": (
                "I can help with returns. "
                "Please provide the product category "
                "and the reason for the return. "
                "For example: "
                "'Electronics, defective'."
            )
        }

    # -------------------------
    # FALLBACK
    # -------------------------

    return get_fallback_message()


def get_fallback_message():
    return {
        "intent": "unmatched",
        "response": (
            "I'm sorry, I can only help with checking "
            "Order Status and processing Returns right now. "
            "Let me connect you with a human support agent "
            "who can help you with your specific issue."
        )
    }