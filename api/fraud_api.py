from fastapi import FastAPI
import joblib
import json
import numpy as np
import pandas as pd
import os

# Load the trained model and threshold
model_path = os.path.join(os.path.dirname(__file__), "../models/xgb_model.pkl")
xgb_model = joblib.load(model_path)

threshold_path = os.path.join(os.path.dirname(__file__), "../models/best_threshold.json")
with open(threshold_path, "r") as f:
    best_threshold = json.load(f)["threshold"]

# Initialize FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Fraud Detection API is running!"}

@app.post("/predict/")
def predict_fraud(data: dict):
    try:
        # Convert input data to DataFrame
        df = pd.DataFrame([data])

        # Ensure all features match the trained model
        expected_features = ['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest',
                             'isFlaggedFraud', 'type_CASH_OUT', 'type_DEBIT', 'type_PAYMENT', 'type_TRANSFER']

        df = df.reindex(columns=expected_features, fill_value=0)

        # Get probability of fraud
        prob = xgb_model.predict_proba(df)[:, 1][0]

        # Apply custom threshold
        is_fraud = int(prob > best_threshold)

        # Convert NumPy types to native Python types
        return {"fraud_probability": float(prob), "is_fraud": int(is_fraud)}

    except Exception as e:
        return {"error": str(e)}
