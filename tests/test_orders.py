from Backend.services.orders_services import get_order_status, load_orders


def test_load_orders_has_mock_data():
    orders = load_orders()
    assert len(orders) >= 15
    assert all("order_id" in order and "status" in order for order in orders)


def test_get_order_status_returns_known_status():
    assert get_order_status("ORD-1001") == "Shipped"
    assert get_order_status("ORD-1007") == "Delivered"
