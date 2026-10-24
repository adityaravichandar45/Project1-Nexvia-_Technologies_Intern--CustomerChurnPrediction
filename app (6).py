import streamlit as st
import pandas as pd
import joblib

# 1. Page Configuration
st.set_page_config(page_title="Customer Churn & ROI Dashboard", layout="wide")

st.title(" Customer Churn, Segmentation & ROI Simulator Dashboard")

# 2. Load all saved model and data artifacts using joblib
@st.cache_resource
def load_artifacts():
    model = joblib.load("churn_lgb_model.pkl")
    scaler = joblib.load("scaler.pkl")
    kmeans = joblib.load("kmeans_model.pkl")
    df = pd.read_pickle("processed_churn_data.pkl")
    return model, scaler, kmeans, df

model, scaler, kmeans, df = load_artifacts()

# 3. Sidebar Controls for ROI & Discount Simulator
st.sidebar.header(" Campaign ROI Simulator")
discount_pct = st.sidebar.slider("Select Retention Discount (%)", 0, 50, 15)
retention_cost_per_user = st.sidebar.number_input("Campaign Cost per User ($)", value=10.0)

# 4. High-Level Metrics
total_customers = len(df)
avg_monthly_rev = df["Monthly Charges"].mean()
high_risk_count = int(total_customers * 0.25) # Estimated or derived from model predictions

col1, col2, col3 = st.columns(3)
col1.metric(label="Total Customer Base", value=f"{total_customers:,}")
col2.metric(label="Estimated High-Risk Churners", value=f"{high_risk_count:,}")
col3.metric(label="Avg Monthly Revenue / User", value=f"${avg_monthly_rev:,.2f}")

# 5. ROI Calculation Section
expected_saved_customers = int(high_risk_count * 0.40) # 40% success rate based on uplift
total_campaign_cost = high_risk_count * retention_cost_per_user
expected_revenue_saved = expected_saved_customers * avg_monthly_rev * 12

st.subheader(" Financial Outlook of Retention Campaign")
fin_col1, fin_col2, fin_col3 = st.columns(3)
fin_col1.metric("Total Campaign Cost", f"${total_campaign_cost:,.2f}")
fin_col2.metric("Saved Annual Revenue", f"${expected_revenue_saved:,.2f}")
fin_col3.metric("Net Projected ROI", f"${expected_revenue_saved - total_campaign_cost:,.2f}")

# 6. Display Customer Data & Clusters
st.subheader(" Customer Segmentation Overview")
st.dataframe(df[["CustomerID", "Tenure Months", "Monthly Charges", "CLV", "Segment"]].head(10))