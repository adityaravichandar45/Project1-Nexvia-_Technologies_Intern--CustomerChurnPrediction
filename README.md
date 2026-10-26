# Project1-Nexvia_Technologies_Intern--CustomerChurnPrediction
# End-to-End Customer Churn Prediction, Uplift Modeling & ROI Simulator

An enterprise-grade machine learning and causal inference pipeline built to predict customer churn, estimate customer lifetime, maximize retention campaign efficiency through uplift modeling, and evaluate financial impact via an interactive Streamlit dashboard.

---

## Project Overview
Customer churn is a critical challenge for subscription-based businesses. This project goes beyond standard classification by combining predictive modeling with **survival analysis**, **causal/uplift modeling**, and **financial simulation** to ensure retention budgets are spent only on customers who actually need an incentive to stay.

### Key Capabilities:
1. **Relational Data Ingestion:** Loaded and structured churn data using a local SQLite/PostgreSQL-compatible relational database pattern.
2. **Exploratory Data Analysis (EDA) & Feature Engineering:** Extracted usage trends, tenure groups, monthly spend ratios, and contract impacts.
3. **Churn Classification & Explainability:** Trained a **LightGBM** classifier and interprets global/local feature importance using **SHAP**.
4. **Survival Analysis:** Applied **Kaplan-Meier** estimators and **Cox Proportional Hazards** regression to estimate customer lifetime duration.
5. **Uplift Modeling:** Used **CausalML** to isolate persuadables (customers who respond positively to retention offers) from sure-things and lost causes.
6. **Customer Lifetime Value (CLV) & Clustering:** For segmenting customers by using **K-Means** clustering based on monetary value and behavioral metrics.
7. **Interactive Streamlit ROI Simulator:** Featured a deployed dashboard where stakeholders can adjust discount sliders to compute campaign costs versus saved revenue in real-time.

---

## Tech Stack
* **Language:** Python 3.x
* **Data Manipulation & Ingestion:** Pandas, NumPy, SQLite / PostgreSQL
* **Machine Learning & Modeling:** LightGBM, Scikit-Learn, CausalML, Lifelines, SHAP
* **Model Serialization:** Joblib
* **Web Application & Deployment:** Streamlit

 Deployed  streamlit app :- https://ccpr-fq.streamlit.app/
 

---

