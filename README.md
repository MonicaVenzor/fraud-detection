# Fraud Detection System

Financial fraud is a low-frequency, high-cost event. The challenge is 
not just building a classifier — it's building one that performs well 
on severely imbalanced data without generating excessive false positives 
that block legitimate transactions.

## What it does

End-to-end fraud detection system trained on financial transaction data. 
Takes transaction features as input and returns a fraud probability score 
with a calibrated decision threshold. Deployed via FastAPI with a 
Streamlit interface for interactive testing.

## Stack

`Python` `XGBoost` `FastAPI` `Streamlit` `Docker` `scikit-learn` `SMOTE`

## Technical decisions

Class imbalance was handled with SMOTE oversampling on the minority 
class. The decision threshold was optimized separately from model 
training to balance precision and recall for the fraud detection 
use case, where false negatives (missed fraud) are more costly than 
false positives.

Model: XGBoost with custom probability threshold. Evaluation metrics: 
Precision, Recall, F1-score.

## API

```
POST /predict/
```

Input: transaction features (amount, balance deltas, transaction type).
Output: fraud probability and binary classification.

## Run locally

```bash
git clone https://github.com/MonicaVenzor/fraud-detection.git
cd fraud-detection
pip install -r api/requirements.txt
uvicorn api.fraud_api:app --reload
```

API available at: `http://127.0.0.1:8000/docs`

## Structure

```
fraud_detection_api/
├── api/
├── models/
├── notebooks/
├── streamlit_app/
└── README.md
```

## Author

Mónica Venzor · [LinkedIn](https://linkedin.com/in/monicavenzor) · 
[GitHub](https://github.com/MonicaVenzor)
