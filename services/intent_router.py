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

        # Common products mapped to their dataset category.
        # This allows natural messages such as:
        # "I want to return my headphones because they are defective."
        product_categories = {
            "headphones": "Electronics",
            "earbuds": "Electronics",
            "keyboard": "Electronics",
            "mouse": "Electronics",
            "monitor": "Electronics",
            "smartwatch": "Electronics",
            "speaker": "Electronics",
            "charger": "Electronics",
            "webcam": "Electronics",
            "ssd": "Electronics",
            "hard drive": "Electronics",
            "usb-c hub": "Electronics",
            "tablet": "Electronics",
            "laptop": "Electronics",

            "phone case": "Accessories",
            "tablet case": "Accessories",
            "laptop stand": "Accessories",
            "monitor arm": "Accessories",

            "chair": "Home Goods",
            "office chair": "Home Goods",
            "desk lamp": "Home Goods"
        }

        category = None
        reason = None

        # First look for an exact category.
        for item in categories:
            if item.lower() in message_lower:
                category = item
                break

        # If no category was found, look for a known product.
        if category is None:
            for product, product_category in product_categories.items():
                if product in message_lower:
                    category = product_category
                    break

        # Find the reason.
        for item in reasons:
            if item.lower() in message_lower:
                reason = item
                break

        # If both category and reason were found,
        # send them to the return service.
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