import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "orders.json"


def load_orders():
    """Load orders from the JSON dataset."""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_order_status(order_id):
    """Look up an order by ID and return its status."""
    orders = load_orders()

    order_id = order_id.strip().upper()

    for order in orders:
        if order["order_id"].upper() == order_id:
            return {
                "found": True,
                "order_id": order["order_id"],
                "status": order["status"],
                "message": (
                    f"Order {order['order_id']} is currently "
                    f"{order['status']}."
                )
            }

    return {
        "found": False,
        "message": (
            f"I couldn't find order {order_id}. "
            "Please check the order ID and try again."
        )
    }