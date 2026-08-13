import json
from pathlib import Path


DATA_FILE = (
    Path(__file__).parent.parent
    / "test_data"
    / "orders.json"
)


def load_orders():
    """Load orders from the JSON dataset."""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_order_status(order_id):
    """Return the status of an order using its order ID."""
    orders = load_orders()

    for order in orders:
        if order["order_id"].upper() == order_id.upper():
            return order["status"]

    return None