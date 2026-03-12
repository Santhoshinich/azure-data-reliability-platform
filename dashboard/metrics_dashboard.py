from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parents[1]

metrics_path = BASE_DIR / "metrics" / "pipeline_metrics.csv"

st.title("Data Pipeline Observability Dashboard")

df = pd.read_csv(metrics_path)

df["timestamp"] = pd.to_datetime(df["timestamp"])

st.subheader("Pipeline Metrics")

st.line_chart(df.set_index("timestamp")["row_count"])

st.subheader("Average Transaction Amount")

st.line_chart(df.set_index("timestamp")["avg_amount"])

st.subheader("Fraud Rate")

st.line_chart(df.set_index("timestamp")["fraud_rate"])

st.dataframe(df)