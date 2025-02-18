import requests

BASE_URL = "https://fraud-detection-9rz0.onrender.com"

def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Fraud Detection API is running!"}

def test_predict():
    sample_data = {
        "step": 1,
        "amount": 5000,
        "oldbalanceOrg": 10000,
        "newbalanceOrig": 5000,
        "oldbalanceDest": 0,
        "newbalanceDest": 0,
        "isFlaggedFraud": 0,
        "type_CASH_OUT": 1,
        "type_DEBIT": 0,
        "type_PAYMENT": 0,
        "type_TRANSFER": 0
    }
    response = requests.post(f"{BASE_URL}/predict/", json=sample_data)
    assert response.status_code == 200
    json_response = response.json()
    assert "fraud_probability" in json_response
    assert "is_fraud" in json_response
