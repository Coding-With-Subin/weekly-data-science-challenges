# Week 8: Can We Predict Which Customers Will Churn?

**Question:** Can a model predict which individual customers will churn, and how should a classifier be judged when only 1 in 4 customers churns?

First classification week. It reuses the Week 4 data and engineered features (`Tenure_Group`, `Total_Services`) and adds one new skill: training a classifier and judging it with accuracy, precision, recall, F1, and a confusion matrix.

**Dataset:** Telco Customer Churn (Kaggle), same file as Week 4: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
**Tools:** Python, Pandas, scikit-learn, Matplotlib, Seaborn

## Structure

```text
week08-churn-prediction/
├── data/Telco-Customer-Churn.csv     raw data (same as Week 4)
├── scripts/
│   ├── prepare_data.py               Week 4 cleaning + features, plus encoding
│   ├── train_model.py                trains baseline + 2 models, prints metrics, saves models
│   └── predict.py                    scores customers with the saved model
├── notebooks/analysis.ipynb          full walkthrough with charts
├── model/
│   ├── churn_model_default.joblib    Logistic Regression
│   ├── churn_model_balanced.joblib   Logistic Regression, class_weight="balanced"
│   └── test_predictions.csv          churn probability for every test customer
├── charts/                           all exported charts
└── README.md
```

## How to run

Python 3.12 or 3.13 is recommended. Install the packages from the `requirements.txt` at the root of the repository:

```bash
pip install -r ../requirements.txt
cd scripts
python train_model.py      # prints the metrics table, saves both models
python predict.py          # scores the 5 highest-risk test customers
```

Or open `notebooks/analysis.ipynb` for the full walkthrough. It uses relative paths (`../data/...`), so run it from inside the `notebooks/` folder with the folder structure intact.

## Results (20% held-out test set, 1,409 customers)

| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Baseline (never predict churn) | 0.735 | 0.000 | 0.000 | 0.000 |
| Logistic Regression | 0.801 | 0.653 | 0.529 | 0.585 |
| Logistic Regression (balanced) | 0.733 | 0.498 | 0.794 | 0.612 |

ROC AUC is 0.841 for both models.

| Model | Churners caught (of 374) | False alarms |
|---|---|---|
| Logistic Regression | 198 | 105 |
| Logistic Regression (balanced) | 297 | 299 |

## Key finding (bonus mystery question)

Doing nothing already scores 73.5% accuracy, so the default model's 80% is less impressive than it looks. The model ranks customers well (AUC 0.84), but at the default cutoff it catches only 198 of 374 churners.

The balanced model's accuracy falls back to the baseline, yet it catches 297 of 374 churners, for about 2 extra false alarms per extra churner caught. Both models rank customers equally well; balancing only moves the cutoff. So the balanced model is not worse, it makes a different trade.

Which one to hand to a retention team depends on cost. The balanced model is worth it if saving one churner is worth more than about 2 wasted retention calls. If calls or offers are expensive, the default model is the safer choice.

## What drives churn (raw rates)

- Month-to-month contracts churn at 43%, one-year at 11%, two-year at 3%
- Fiber optic customers churn at 42%, DSL at 19%
- Customers in their first 12 months churn at 47%

These are raw rates, not causes. The data shows where churn concentrates, not why.

## Business recommendations

1. Use the balanced model for retention outreach, provided a saved customer is worth more than about 2 wasted calls.
2. Push month-to-month customers toward longer contracts.
3. Review fiber optic pricing and service quality, and first-year onboarding.
4. Report recall and precision next to accuracy. Accuracy alone makes the model look better than it is.

## Charts

Class balance, confusion matrix, confusion matrices compared, metrics comparison, ROC curve, churn drivers.