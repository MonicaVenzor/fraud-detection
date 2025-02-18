🛡️ Fraud Detection API using Machine Learning
🚀 A FastAPI-powered fraud detection system using XGBoost. This API predicts fraudulent transactions based on financial data.

📌 Features
✔ FastAPI for real-time fraud prediction
✔ XGBoost Model trained on financial transactions
✔ Custom Fraud Probability Threshold for better accuracy
✔ Endpoints for Real-Time Predictions
✔ Docker Support (Optional for Deployment)

📂 fraud_detection_api/
   ├── 📂 api/
   │   ├── fraud_api.py
   │   ├── requirements.txt
   ├── 📂 models/
   │   ├── xgb_model.pkl
   │   ├── best_threshold.json
   ├── 📂 notebooks/
   │   ├── fraud_detection.ipynb
   ├── 📂 raw_data/
   ├── README.md
   ├── .gitignore

🚀 Installation & Usage

1️⃣ Clone the Repository
git clone https://github.com/YOUR_GITHUB_USERNAME/fraud_detection_api.git
cd fraud_detection_api

2️⃣ Create a Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r api/requirements.txt

3️⃣ Run the FastAPI Server
uvicorn api.fraud_api:app --reload
The API will be available at 👉 http://127.0.0.1:8000/docs

🌐 API Endpoints
Method	Endpoint	Description
GET	/	Home Page
POST	/predict/	Predict Fraudulent Transactions

📌 Example Request (JSON)
{
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

📌 Example Response
{
    "fraud_probability": 0.998,
    "is_fraud": 1
}

🛠️ Deployment

📦 Docker Deployment (Optional)
1️⃣ Build the Docker Image
docker build -t fraud-detection-api .
2️⃣ Run the API in a Container
docker run -p 8000:8000 fraud-detection-api

📦 Deploy to Render
1️⃣Link GitHub repo to Render.com
2️⃣Set root directory as api/
    Use these commands:
    Build Command: pip install -r requirements.txt
    Start Command: uvicorn fraud_api:app --host 0.0.0.0 --port 10000

3️⃣Deploy and access API at: https://your-app-name.onrender.com

🎯 Next Steps
🔹 Create a Streamlit Dashboard to visualize fraud trends
🔹 Improve Model Performance with feature engineering

👨‍💻 🏆 Author: Monica Venzor
📌 GitHub Repo: fraud-detection
