[demo video.zip](https://github.com/user-attachments/files/30019978/demo.video.zip)


# 🏦 SentinelBank AI

# Intelligent Banking Security & Credit Risk Assessment Platform

SentinelBank AI is a next-generation AI-powered banking intelligence platform that combines **Machine Learning**, **Risk Analytics**, and **Web Technologies** to assist financial institutions in detecting fraudulent credit card transactions and evaluating credit card applications in real time.

Unlike conventional banking systems that rely solely on rule-based verification, SentinelBank AI integrates predictive analytics and automated decision-making to improve banking security, reduce financial losses, and accelerate credit approval workflows.

---

# Key Features

## Credit Card Approval Engine

The platform evaluates customer applications using multiple financial parameters.

### Applicant Information

- Customer Details
- PAN Validation
- Age Verification
- Annual Income
- Employment Status
- Existing Loans
- Credit Score
- Requested Credit Limit

### Document Upload

Supports:

- PDF
- CSV
- Excel (.xlsx)

Uploaded bank statements are automatically processed before prediction.

### Decision Output

The AI system predicts:

- Approved
- Rejected

with

- Confidence Score
- Risk Level
- Decision Explanation

All applications are securely stored inside the MySQL database.

---

# AI Fraud Detection Engine

SentinelBank AI includes a fraud detection engine trained using supervised machine learning.

The model evaluates transaction characteristics and predicts whether a transaction is fraudulent.

### Input

- Transaction Time
- Transaction Amount

### Output

- Legitimate Transaction
- Fraudulent Transaction
- Prediction Confidence

---

# Machine Learning Model

Algorithm:

Random Forest Classifier

Training Dataset:

Kaggle Credit Card Fraud Detection Dataset

Dataset Statistics

- Total Transactions: 284,807
- Legitimate Transactions: 284,315
- Fraudulent Transactions: 492

Model Performance

- Accuracy: 99.81%
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

# Analytics Dashboard

The web dashboard provides real-time banking analytics.

Includes

- Total Transactions
- Fraudulent Transactions
- Legitimate Transactions
- Fraud Rate
- Credit Applications
- Approved Applications
- Rejected Applications
- Model Accuracy

Visualizations

- Pie Charts
- Banking Statistics
- Performance Cards
- Recent Banking Activity

---

# Dataset Analysis

Users can upload banking datasets for instant AI analysis.

Supported Formats

- CSV
- Excel
- PDF

The application automatically summarizes

- Total Transactions
- Fraud Count
- Legitimate Count
- Fraud Percentage

---

# Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Google Fonts

## Backend

- Python
- Flask

## Database

- MySQL

## Machine Learning

- Scikit-Learn
- Random Forest
- Joblib

## Data Processing

- Pandas
- NumPy

---

# Project Structure

SentinelBankAI/

├── app.py

├── train_model.py

├── requirements.txt

├── README.md

├── datasets/

│ └── creditcard.csv

├── trained_models/

│ └── fraud_model.pkl

├── templates/

├── uploads/

├── static/

└── database/

---

# Database

Database Name

bank_security_ai

Main Table

credit_applications

Stored Information

- Applicant Name
- PAN Number
- Age
- Income
- Credit Score
- Employment Status
- Existing Loans
- Requested Credit Limit
- Approval Result
- Timestamp

---

# Installation

Clone Repository

git clone <repository-url>

Move to Project

cd SentinelBankAI

Install Dependencies

pip install -r requirements.txt

Train Model

python train_model.py

Run Application

python app.py

Open Browser

http://127.0.0.1:5000

---

# Machine Learning Workflow

Dataset

↓

Data Cleaning

↓

Feature Engineering

↓

Random Forest Training

↓

Model Serialization

↓

Flask Backend

↓

Fraud Prediction

↓

Dashboard Visualization

---

# Security Features

- PAN Validation
- Secure File Upload
- Credit Risk Evaluation
- Fraud Detection
- Confidence Score
- Database Logging
- Secure Banking Workflow

---

# Future Enhancements

- Multi-Factor Authentication
- Admin Dashboard
- OTP Verification
- Aadhaar Integration
- PAN API Verification
- Email Notifications
- SMS Alerts
- Banking APIs
- Real-Time Fraud Monitoring
- Deep Learning Models
- Explainable AI (SHAP)
- Docker Deployment
- REST APIs
- Mobile Banking Support

---

# Academic Contribution

SentinelBank AI demonstrates the practical application of Artificial Intelligence in financial services by integrating fraud detection and credit risk assessment into a unified banking platform.

The system highlights how machine learning can improve operational efficiency, strengthen fraud prevention, and support intelligent decision-making in modern banking environments.

---

# Disclaimer

This project is developed exclusively for academic and research purposes. It is not intended for production banking environments without appropriate regulatory compliance, security auditing, and financial institution approval.

---

# Author

Parinita

B.Tech — Computer Science & Engineering

Academic Project • 2026

---

# License

MIT License
