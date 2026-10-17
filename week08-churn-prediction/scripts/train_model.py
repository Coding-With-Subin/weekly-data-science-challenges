"""
train_model.py
Trains the Week 8 churn classifiers. Run from the scripts/ folder:

    python train_model.py

Compares three things on the same held-out test set:
  1. Baseline: predict "no churn" for everyone
  2. Logistic Regression (default)
  3. Logistic Regression (class_weight="balanced")

Saves both models to ../model/ and the test predictions to a CSV.
"""
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from prepare_data import load_and_prepare, build_features


def score(y_true, y_pred, y_prob=None):
    out = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    }
    if y_prob is not None:
        out["roc_auc"] = roc_auc_score(y_true, y_prob)
    return out


def main():
    df = load_and_prepare("../data/Telco-Customer-Churn.csv")
    X, y = build_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 1. Baseline: always predict "no churn"
    baseline_pred = pd.Series(0, index=y_test.index)

    # 2 and 3. Logistic Regression (scaling needed so the optimizer converges)
    default = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
    balanced = make_pipeline(StandardScaler(),
                             LogisticRegression(max_iter=1000, class_weight="balanced"))
    default.fit(X_train, y_train)
    balanced.fit(X_train, y_train)

    results = {
        "Baseline (never churn)": score(y_test, baseline_pred),
        "Logistic Regression": score(y_test, default.predict(X_test),
                                     default.predict_proba(X_test)[:, 1]),
        "Logistic Regression (balanced)": score(y_test, balanced.predict(X_test),
                                                balanced.predict_proba(X_test)[:, 1]),
    }
    print(pd.DataFrame(results).T.round(3).to_string())

    for name, model in [("default", default), ("balanced", balanced)]:
        tn, fp, fn, tp = confusion_matrix(y_test, model.predict(X_test)).ravel()
        print(f"\n{name}: caught {tp} of {tp + fn} churners, "
              f"flagged {tp + fp} customers ({fp} false alarms)")

    joblib.dump({"model": default, "columns": list(X.columns)}, "../model/churn_model_default.joblib")
    joblib.dump({"model": balanced, "columns": list(X.columns)}, "../model/churn_model_balanced.joblib")

    out = X_test.copy()
    out["customerID"] = df.loc[X_test.index, "customerID"]
    out["actual_churn"] = y_test
    out["churn_probability"] = balanced.predict_proba(X_test)[:, 1].round(3)
    out["predicted_churn"] = balanced.predict(X_test)
    out[["customerID", "actual_churn", "churn_probability", "predicted_churn"]].to_csv(
        "../model/test_predictions.csv", index=False)
    print("\nModels and test predictions saved to ../model/")


if __name__ == "__main__":
    main()
