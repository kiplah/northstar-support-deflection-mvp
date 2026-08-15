import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_order_status_1(client):
    response = client.post("/api/chat", json={"message": "What is the status of order ORD-1001?"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["intent"] == "order_status"
    assert "Order ORD-1001 is currently Shipped." in data["response"]

def test_order_status_2(client):
    response = client.post("/api/chat", json={"message": "where is my order 1002?"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["intent"] == "order_status"
    assert "Order ORD-1002 is currently Processing." in data["response"]

def test_order_status_3(client):
    response = client.post("/api/chat", json={"message": "track order ORD-1003"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["intent"] == "order_status"
    assert "Order ORD-1003 is currently Delivered." in data["response"]

def test_order_status_4(client):
    response = client.post("/api/chat", json={"message": "order status 1004"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["intent"] == "order_status"
    assert "Order ORD-1004 is currently Cancelled." in data["response"]

def test_order_status_5(client):
    response = client.post("/api/chat", json={"message": "track my order 1005"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["intent"] == "order_status"
    assert "Order ORD-1005 is currently Shipped." in data["response"]

def test_returns_1(client):
    response = client.post("/api/chat", json={"message": "I want to return Electronics, it is defective."})
    assert response.status_code == 200
    data = response.get_json()
    assert data["intent"] == "returns"
    assert "Item is eligible for return." in data["response"]

def test_returns_2(client):
    response = client.post("/api/chat", json={"message": "Return Accessories, I changed mind."})
    assert response.status_code == 200
    data = response.get_json()
    assert data["intent"] == "returns"
    assert "Item is eligible for return." in data["response"]

def test_returns_3(client):
    response = client.post("/api/chat", json={"message": "Refund Home Goods, wrong item."})
    assert response.status_code == 200
    data = response.get_json()
    assert data["intent"] == "returns"
    assert "Item is eligible for return." in data["response"]

def test_returns_4(client):
    response = client.post("/api/chat", json={"message": "I want a refund for Apparel because wrong size."})
    assert response.status_code == 200
    data = response.get_json()
    assert data["intent"] == "returns"
    assert "Item is eligible for return." in data["response"]

def test_returns_5(client):
    response = client.post("/api/chat", json={"message": "return Software, changed mind."})
    assert response.status_code == 200
    data = response.get_json()
    assert data["intent"] == "returns"
    assert "This reason is not covered by the return policy." in data["response"]