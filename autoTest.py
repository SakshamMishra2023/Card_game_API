import pytest
import httpx

BASE_URL = "http://127.0.0.1:8001"

def test_join_game():
    response = httpx.post(f"{BASE_URL}/join", json={"name": "Player1"})
    assert response.status_code == 200
    assert "joined the game" in response.json()["message"]

def test_place_bet():
    httpx.post(f"{BASE_URL}/join", json={"name": "Player1"})
    response = httpx.post(f"{BASE_URL}/bet", json={"name": "Player1", "amount": 10})
    assert response.status_code == 200
    assert "placed a bet" in response.json()["message"]

def test_fold():
    httpx.post(f"{BASE_URL}/join", json={"name": "Player1"})
    response = httpx.post(f"{BASE_URL}/fold", json={"name": "Player1"})
    assert response.status_code == 200
    assert "folded" in response.json()["message"]
