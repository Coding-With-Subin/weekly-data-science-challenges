"""
prepare_data.py
Carries forward the Week 6 cleaning + feature engineering so Week 7
starts from the same trusted dataset instead of re-guessing it.
"""
import pandas as pd
import numpy as np


def load_and_prepare(csv_path="../data/used_cars.csv", reference_year=2025):
    df = pd.read_csv(csv_path)

    # --- Clean price and milage (Week 6) ---
    df["price"] = (df["price"].str.replace("$", "", regex=False)
                              .str.replace(",", "", regex=False).astype(float))
    df["milage"] = (df["milage"].str.replace(" mi.", "", regex=False)
                                .str.replace(",", "", regex=False).astype(float))

    # --- Fix split brand names (Week 6) ---
    tails = {"Land": "Rover ", "Aston": "Martin ", "Alfa": "Romeo "}
    full_names = {"Land": "Land Rover", "Aston": "Aston Martin", "Alfa": "Alfa Romeo"}
    for short, tail in tails.items():
        mask = df["brand"] == short
        df.loc[mask, "model"] = df.loc[mask, "model"].str.replace(tail, "", n=1, regex=False)
        df.loc[mask, "brand"] = full_names[short]

    # --- Missing values, with judgment (Week 6) ---
    bad_fuel = df["fuel_type"].isna() | df["fuel_type"].isin(["–", "not supported"])
    is_electric = df["engine"].str.contains("Electric Motor", case=False, na=False)
    df.loc[bad_fuel & is_electric, "fuel_type"] = "Electric"
    df.loc[df["fuel_type"].isna() | df["fuel_type"].isin(["–", "not supported"]), "fuel_type"] = "Unknown"
    df["clean_title"] = df["clean_title"].fillna("Not listed")
    df["accident"] = df["accident"].fillna("Unknown")

    # --- Drop the one impossible price (Week 6) ---
    price_suspect = (df["brand"] == "Maserati") & (df["model_year"] == 2005) & (df["price"] > 2_000_000)
    df = df[~price_suspect].copy()

    # --- Feature engineering (Week 6) ---
    df["car_age"] = (reference_year - df["model_year"]).replace(0, 1)
    df["mileage_per_year"] = (df["milage"] / df["car_age"]).round(0)

    luxury_brands = ["BMW", "Mercedes-Benz", "Audi", "Lexus", "Porsche", "Jaguar", "Land Rover",
                     "Bentley", "Maserati", "Ferrari", "Lamborghini", "Aston Martin", "Rolls-Royce",
                     "McLaren", "Maybach", "Bugatti", "Lotus", "Alfa Romeo", "Genesis"]
    df["brand_tier"] = np.where(df["brand"].isin(luxury_brands), "Luxury", "Economy")

    # --- New for Week 7: encode brand_tier for modeling ---
    df["brand_tier_num"] = (df["brand_tier"] == "Luxury").astype(int)

    return df


FEATURES = ["car_age", "mileage_per_year", "brand_tier_num"]
TARGET = "price"
