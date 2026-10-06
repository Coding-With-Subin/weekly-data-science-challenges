"""
train_model.py
Trains the Week 7 Linear Regression model on the Week 6 cleaned,
feature-engineered used car data. Run from the scripts/ folder:

    python train_model.py

Saves the fitted model to ../model/price_model.joblib and prints
RMSE, MAE, and R-squared on the held-out test set.
"""
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from prepare_data import load_and_prepare, FEATURES, TARGET


def main():
    df = load_and_prepare("../data/used_cars.csv")

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    rmse = mean_squared_error(y_test, y_pred) ** 0.5
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Features used:", FEATURES)
    print("Coefficients: ", dict(zip(FEATURES, model.coef_.round(2))))
    print(f"Intercept:     {model.intercept_:.2f}")
    print()
    print(f"RMSE:        ${rmse:,.0f}")
    print(f"MAE:         ${mae:,.0f}")
    print(f"R-squared:   {r2:.3f}")

    joblib.dump(model, "../model/price_model.joblib")
    print("\nModel saved to ../model/price_model.joblib")

    # Save test-set predictions for later inspection (e.g. the mystery question)
    results = X_test.copy()
    results["actual_price"] = y_test
    results["predicted_price"] = y_pred.round(0)
    results["error"] = (results["predicted_price"] - results["actual_price"]).round(0)
    results.to_csv("../model/test_predictions.csv", index=False)
    print("Test predictions saved to ../model/test_predictions.csv")


if __name__ == "__main__":
    main()
