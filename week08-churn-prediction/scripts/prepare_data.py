"""
prepare_data.py
Carries forward the Week 4 cleaning and feature engineering (TotalCharges fix,
Churn_Flag, Tenure_Group, Total_Services) and adds the Week 8 step:
turning every column into numbers a classifier can use.
"""
import pandas as pd

SERVICE_COLS = ["OnlineSecurity", "OnlineBackup", "DeviceProtection",
                "TechSupport", "StreamingTV", "StreamingMovies"]
TARGET = "Churn_Flag"


def tenure_group(months):
    if months <= 12:
        return "New (0-12mo)"
    elif months <= 48:
        return "Established (12-48mo)"
    return "Loyal (48mo+)"


def load_and_prepare(csv_path="../data/Telco-Customer-Churn.csv"):
    df = pd.read_csv(csv_path)

    # --- Week 4: clean TotalCharges (blank for the 11 customers with tenure = 0) ---
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)
    df[TARGET] = (df["Churn"] == "Yes").astype(int)

    # --- Week 4: engineered features ---
    df["Tenure_Group"] = df["tenure"].apply(tenure_group)
    df["Total_Services"] = df[SERVICE_COLS].apply(lambda row: (row == "Yes").sum(), axis=1)
    return df


def build_features(df):
    """Week 8: one-hot encode every text column so a model can use it."""
    X = pd.get_dummies(df.drop(columns=["customerID", "Churn", TARGET]), drop_first=True)
    y = df[TARGET]
    return X, y
