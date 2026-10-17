"""
predict.py
Loads the saved balanced model and scores customers for churn risk.
Run from the scripts/ folder after train_model.py:

    python predict.py
"""
import joblib
import pandas as pd

from prepare_data import load_and_prepare, build_features


def predict_churn(customer_ids, model_path="../model/churn_model_balanced.joblib"):
    saved = joblib.load(model_path)
    model, columns = saved["model"], saved["columns"]

    df = load_and_prepare("../data/Telco-Customer-Churn.csv")
    X, _ = build_features(df)
    X = X.reindex(columns=columns, fill_value=0)   # same columns, same order as training

    mask = df["customerID"].isin(customer_ids)
    out = pd.DataFrame({
        "customerID": df.loc[mask, "customerID"],
        "churn_probability": model.predict_proba(X[mask])[:, 1].round(3),
        "predicted_churn": model.predict(X[mask]),
    })
    return out.sort_values("churn_probability", ascending=False)


if __name__ == "__main__":
    # Demo: the 5 test-set customers the model rates as most likely to churn
    test = pd.read_csv("../model/test_predictions.csv")
    top5 = test.sort_values("churn_probability", ascending=False).head(5)["customerID"]
    print(predict_churn(top5).to_string(index=False))
