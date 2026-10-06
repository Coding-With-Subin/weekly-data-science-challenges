# Week 7: Can We Predict a Used Car's Price?

**Question:** Do the features engineered last week (car_age, mileage_per_year, brand_tier) actually predict price, and where does a simple model fall short?

First ML week. Cleaning and feature engineering carried forward from Week 6; this week trains and evaluates a Linear Regression model.

**Dataset:** Used Car Price Prediction (Kaggle), same file as Week 6
**Tools:** Python, Pandas, scikit-learn, Matplotlib, Seaborn

## Structure

```
week07-price-prediction/
├── data/used_cars.csv            raw data (same as Week 6)
├── scripts/
│   ├── prepare_data.py           Week 6 cleaning + feature engineering, reused
│   ├── train_model.py            trains the model, saves it, prints metrics
│   └── predict.py                loads the saved model, predicts on example cars
├── notebooks/analysis.ipynb      full walkthrough: EDA, training, evaluation, mystery question
├── model/
│   ├── price_model.joblib        saved trained model
│   └── test_predictions.csv      every test-set prediction, with error
├── charts/                       all exported charts
└── README.md
```

## How to run

```bash
cd scripts
python train_model.py      # trains model, prints RMSE/MAE/R-squared, saves model
python predict.py          # loads saved model, predicts on 3 example cars
```

Or open `notebooks/analysis.ipynb` for the full walkthrough. Uses relative paths (`../data/...`), so run it from inside the `notebooks/` folder, with the folder structure intact.

## Model

Linear Regression, 3 features: `car_age`, `mileage_per_year`, `brand_tier_num` (0/1).

| Metric | Full test set | Cars under $200k only |
|---|---|---|
| RMSE | $94,418 | $25,867 |
| MAE | $26,937 | N/A |
| R-squared | 0.076 | 0.325 |

## Key finding (bonus mystery question)

Low overall R-squared isn't noise, it's a dozen exotic cars (Bugatti, Rolls-Royce, Lamborghini, Porsche Carrera GT) that three simple features can't represent. Scored on ordinary cars alone, R-squared roughly quadruples. Fix isn't more data, it's a third brand_tier category for exotics instead of lumping them with Luxury.

## Note on metrics

Accuracy and F1 score are classification metrics. Price is continuous, so this project uses RMSE, MAE, and R-squared instead, plus a correlation heatmap, a predicted-vs-actual plot, and a residual plot.