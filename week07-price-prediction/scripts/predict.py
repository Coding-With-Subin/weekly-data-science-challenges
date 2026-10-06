"""
predict.py
Loads the saved model and predicts price for one or more cars.
Run from the scripts/ folder after train_model.py:

    python predict.py
"""
import joblib
import pandas as pd
from prepare_data import FEATURES


def predict_price(car_age, mileage_per_year, brand_tier):
    """
    car_age: int, years
    mileage_per_year: float
    brand_tier: "Luxury" or "Economy"
    """
    model = joblib.load("../model/price_model.joblib")
    brand_tier_num = 1 if brand_tier == "Luxury" else 0
    X = pd.DataFrame([[car_age, mileage_per_year, brand_tier_num]], columns=FEATURES)
    return float(model.predict(X)[0])


if __name__ == "__main__":
    examples = [
        {"car_age": 3, "mileage_per_year": 12000, "brand_tier": "Economy"},
        {"car_age": 3, "mileage_per_year": 12000, "brand_tier": "Luxury"},
        {"car_age": 10, "mileage_per_year": 15000, "brand_tier": "Economy"},
    ]
    for ex in examples:
        price = predict_price(**ex)
        print(f"{ex} -> predicted price: ${price:,.0f}")
