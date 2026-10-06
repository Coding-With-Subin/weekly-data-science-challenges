# Weekly Data Science Challenges

A growing weekly series of data science and machine learning projects, starting with real-world data analysis and feature engineering, and building toward full ML workflows. Each week adds a new skill on top of the last, using Python, Pandas, and industry-standard tools.

## How This Series Works

Each week lives in its own folder with a complete, self-contained project: dataset, notebook, charts, and a README explaining the question, the findings, and the business recommendations. Skills build progressively, moving from analysis fundamentals toward the preprocessing, feature work, and modeling that real ML projects depend on:

| Week | Project | Core Skill |
|------|---------|-----------|
| 01 | [Superstore Customer Analysis](week01-superstore-customer/) | Pandas fundamentals, exploration |
| 02 | [Superstore Sales Trends](week02-superstore-sales-trends/) | Grouping and aggregation, trend analysis |
| 03 | [Superstore Profitability](week03-superstore-profitability/) | Business-question-driven analysis |
| 04 | [Telco Customer Churn](week04-telco-churn/) | Feature engineering |
| 05 | [Tech Layoffs](week05-tech-layoffs/) | Data preprocessing and cleaning |
| 06 | [Used Car Price Analysis](week06-used-cars/) | Cleaning with judgment and feature engineering on clean data |
| 07 | [Used Car Price Prediction](week07-price-prediction/) | First ML model: Linear Regression, train/test split, evaluation |

More weeks are added regularly, moving deeper into full machine learning workflows (model training, evaluation, and deployment-style projects) as the series progresses.

## Latest Week

**Week 07: Can We Predict a Used Car's Price?**

First machine learning week. Reuses Week 6's cleaned data and engineered features (car_age, mileage_per_year, brand_tier) to train a Linear Regression model. Overall R-squared is low (0.08), but tracing the error shows why: a dozen exotic cars (Bugatti, Rolls-Royce, Lamborghini) overwhelm the score. Scored on ordinary cars alone, R-squared roughly quadruples (0.33). The fix isn't more data, it's a third brand_tier category for exotics.

## Tools Used Across the Series

* Python
* Pandas
* NumPy
* Matplotlib / Seaborn
* SciPy (where statistical testing is relevant)
* Scikit-learn (model training and evaluation, starting Week 07)
* Joblib (model persistence)

## Repository Structure

```text
weekly-data-science-challenges/
│
├── README.md                     ← you are here
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── week01-superstore-customer/
│   ├── README.md
│   ├── data/
│   ├── notebooks/analysis.ipynb
│   └── reports/figures/
│
├── week02-superstore-sales-trends/
│   ├── README.md
│   ├── data/
│   ├── notebooks/analysis.ipynb
│   └── reports/figures/
│
├── week03-superstore-profitability/
│   ├── README.md
│   ├── data/
│   ├── notebooks/analysis.ipynb
│   └── reports/figures/
│
├── week04-telco-churn/
│   ├── README.md
│   ├── data/
│   ├── notebooks/analysis.ipynb
│   └── reports/figures/
│
├── week05-tech-layoffs/
│   ├── README.md
│   ├── data/
│   ├── notebooks/analysis.ipynb
│   └── reports/figures/
│
├── week06-used-cars/
│   ├── README.md
│   ├── data/raw/
│   ├── notebooks/analysis.ipynb
│   └── reports/figures/
│
└── week07-price-prediction/
    ├── README.md
    ├── data/
    ├── scripts/
    │   ├── prepare_data.py
    │   ├── train_model.py
    │   └── predict.py
    ├── notebooks/analysis.ipynb
    ├── model/
    └── charts/
```

Each week's folder is independently runnable. Its own README has the specific dataset link, setup steps, and findings for that week.

## How to Run Any Week

```bash
git clone https://github.com/Coding-With-Subin/weekly-data-science-challenges.git
cd weekly-data-science-challenges
pip install -r requirements.txt
```

Then open the specific week's folder, download its dataset per that week's README, and run its notebook.

## License

This project is licensed under the MIT License. See the LICENSE file for details. Each dataset used is sourced from Kaggle and remains subject to its original licensing and usage terms.

## About

This series is part of an ongoing weekend data challenge, where a new dataset and business question are released each week to practice real-world data analysis and, increasingly, machine learning skills, one deliberate skill at a time.