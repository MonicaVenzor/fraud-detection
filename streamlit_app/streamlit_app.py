import streamlit as st
import requests

# Streamlit UI
st.title("Fraud Detection API 🚀")
st.markdown("Enter transaction details to check if it's fraudulent.")

# User input fields
step = st.number_input("Step", min_value=1, value=1)
amount = st.number_input("Amount", min_value=0, value=5000)
oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0, value=10000)
newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0, value=5000)
oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0, value=0)
newbalanceDest = st.number_input("New Balance (Destination)", min_value=0, value=0)
isFlaggedFraud = st.selectbox("Is Flagged as Fraud?", [0, 1])

# Transaction Type (One-Hot Encoded)
st.markdown("### Transaction Type")
transaction_type = st.radio("Select Transaction Type:", ["CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"])
type_mapping = {
    "CASH_OUT": [1, 0, 0, 0],
    "DEBIT": [0, 1, 0, 0],
    "PAYMENT": [0, 0, 1, 0],
    "TRANSFER": [0, 0, 0, 1],
}

# Prepare request data
data = {
    "step": step,
    "amount": amount,
    "oldbalanceOrg": oldbalanceOrg,
    "newbalanceOrig": newbalanceOrig,
    "oldbalanceDest": oldbalanceDest,
    "newbalanceDest": newbalanceDest,
    "isFlaggedFraud": isFlaggedFraud,
    "type_CASH_OUT": type_mapping[transaction_type][0],
    "type_DEBIT": type_mapping[transaction_type][1],
    "type_PAYMENT": type_mapping[transaction_type][2],
    "type_TRANSFER": type_mapping[transaction_type][3],
}

# API Call
if st.button("Check Fraud Status"):
    api_url = "https://fraud-detection-9rz0.onrender.com/predict/"
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Fraud Probability: {result['fraud_probability']:.2%}")
        if result["is_fraud"]:
            st.error("⚠️ This transaction is likely **fraudulent**!")
        else:
            st.success("✅ This transaction is **not fraudulent**.")
    else:
        st.error("Error in API call. Check your API deployment.")
