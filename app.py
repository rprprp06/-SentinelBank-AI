import os
import pickle
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "credit_card_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

FEATURE_ORDER = [
    "CODE_GENDER",
    "FLAG_OWN_CAR",
    "FLAG_OWN_REALTY",
    "CNT_CHILDREN",
    "AMT_INCOME_TOTAL",
    "NAME_INCOME_TYPE",
    "NAME_EDUCATION_TYPE",
    "NAME_FAMILY_STATUS",
    "NAME_HOUSING_TYPE",
    "DAYS_BIRTH",
    "DAYS_EMPLOYED",
    "FLAG_MOBIL",
    "FLAG_WORK_PHONE",
    "FLAG_PHONE",
    "FLAG_EMAIL",
    "OCCUPATION_TYPE",
    "CNT_FAM_MEMBERS",
]

MODEL = None
SCALER = None


def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)


if os.path.exists(MODEL_PATH):
    try:
        MODEL = load_pickle(MODEL_PATH)
    except Exception:
        MODEL = None

if os.path.exists(SCALER_PATH):
    try:
        SCALER = load_pickle(SCALER_PATH)
    except Exception:
        SCALER = None


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if MODEL is None:
        return render_template("result.html", prediction_text="Model file not found or could not be loaded.")

    values = {}
    for field in FEATURE_ORDER:
        raw = request.form.get(field, "").strip()
        if field in ["CNT_CHILDREN", "CNT_FAM_MEMBERS"]:
            values[field] = int(raw) if raw.isdigit() else 0
        elif field == "AMT_INCOME_TOTAL":
            try:
                values[field] = float(raw)
            except ValueError:
                values[field] = 0.0
        elif field in ["DAYS_BIRTH", "DAYS_EMPLOYED"]:
            try:
                values[field] = int(raw)
            except ValueError:
                values[field] = 0
        elif field in ["FLAG_MOBIL", "FLAG_WORK_PHONE", "FLAG_PHONE", "FLAG_EMAIL"]:
            values[field] = 1 if raw in ["1", "Y", "y", "yes", "Yes", "true", "True"] else 0
        else:
            values[field] = raw

    df = pd.DataFrame([values], columns=FEATURE_ORDER)

    try:
        if SCALER is not None:
            numeric_columns = [
                "CNT_CHILDREN",
                "AMT_INCOME_TOTAL",
                "DAYS_BIRTH",
                "DAYS_EMPLOYED",
                "CNT_FAM_MEMBERS",
            ]
            df_numeric = df[numeric_columns].astype(float)
            df[numeric_columns] = SCALER.transform(df_numeric)

        prediction = MODEL.predict(df)
        if hasattr(prediction, "tolist"):
            prediction = prediction.tolist()[0]
        if int(prediction) == 1:
            status = "APPROVED"
        else:
            status = "REJECTED"
        return render_template("result.html", prediction_text=f"Credit card application is {status}.")
    except Exception as exc:
        return render_template("result.html", prediction_text=f"Prediction failed: {exc}")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
