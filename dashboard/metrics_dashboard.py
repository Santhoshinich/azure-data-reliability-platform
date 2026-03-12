from pathlib import Path
import pandas as pd
import streamlit as st

# -------------------------
# CONFIG
# -------------------------

st.set_page_config(
    page_title="Data Reliability Platform",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# STYLE
# -------------------------

st.markdown("""
<style>

/* Page background */
.stApp {
background-color: #f5f7fa;
}

/* Header banner */
.header-box {
background:#3b3f45;
padding:22px;
border-radius:10px;
text-align:center;
color:white;
font-size:30px;
font-weight:600;
}

/* Subtitle */
.subtext{
text-align:center;
color:#6b7280;
font-size:16px;
margin-bottom:30px;
}

/* Section titles */
h3{
color:#3b3f45;
}

/* Metric cards */
[data-testid="metric-container"] {
background:white;
border-radius:10px;
padding:15px;
box-shadow:0px 2px 6px rgba(0,0,0,0.08);
}

/* Footer */
.footer{
margin-top:40px;
padding:18px;
text-align:center;
font-size:14px;
background:#3b3f45;
color:white;
border-radius:8px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------

st.markdown("""
<div class="header-box">
📊 Data Reliability & ML Observability Platform
</div>
<div class="subtext">
Monitoring pipeline health, data quality, drift detection and ML performance
</div>
""", unsafe_allow_html=True)

# -------------------------
# LOAD DATA
# -------------------------

BASE_DIR = Path(__file__).resolve().parents[1]
metrics_path = BASE_DIR / "metrics" / "pipeline_metrics.csv"

df = pd.read_csv(metrics_path)
df["timestamp"] = pd.to_datetime(df["timestamp"])

latest = df.iloc[-1]

# -------------------------
# PIPELINE HEALTH
# -------------------------

st.markdown("### 🚦 Pipeline Health")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Row Count", f"{int(latest['row_count']):,}")

with col2:
    st.metric("Avg Transaction ($)", f"{latest['avg_amount']:.2f}")

with col3:
    st.metric("Fraud Rate", f"{latest['fraud_rate']:.4f}")

st.divider()

# -------------------------
# DATA METRICS
# -------------------------

st.markdown("### 📈 Data Observability Metrics")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Row Count Trend")
    st.line_chart(df.set_index("timestamp")["row_count"])

with col2:
    st.subheader("Average Transaction Trend")
    st.line_chart(df.set_index("timestamp")["avg_amount"])

st.subheader("Fraud Rate Trend")
st.line_chart(df.set_index("timestamp")["fraud_rate"])

st.divider()

# -------------------------
# TABLE
# -------------------------

st.markdown("### 📄 Pipeline Metrics History")

st.dataframe(
df.sort_values("timestamp", ascending=False),
use_container_width=True
)

# -------------------------
# FOOTER
# -------------------------

st.markdown("""
<div class="footer">
Data Reliability Monitoring Platform<br><br>
Pipeline Monitoring • Data Quality • Drift Detection • ML Validation<br><br>
Author: <b>Santhoshini Ch</b>
</div>
""", unsafe_allow_html=True)