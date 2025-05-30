import requests

BASE = "http://127.0.0.1:8000"

def test_register_and_login():
    email = "test@example.com"
    password = "testpass"
    # Register
    r = requests.post(f"{BASE}/auth/register", json={"email": email, "password": password, "name": "Test User"})
    assert r.status_code == 200, r.text
    token = r.json()["access_token"]
    # Login
    r = requests.post(f"{BASE}/auth/login", json={"email": email, "password": password})
    assert r.status_code == 200, r.text
    token = r.json()["access_token"]
    # Get profile
    r = requests.get(f"{BASE}/users/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200, r.text
    print("User info:", r.json())

if __name__ == "__main__":
    test_register_and_login()
