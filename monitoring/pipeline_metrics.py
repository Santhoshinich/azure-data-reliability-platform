from pathlib import Path
import pandas as pd
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[1]

data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"
metrics_path = BASE_DIR / "metrics" / "pipeline_metrics.csv"

df = pd.read_parquet(data_path)

metrics = {
    "timestamp": datetime.now(),
    "row_count": len(df),
    "avg_amount": df["amount"].mean(),
    "fraud_rate": df["fraud_label"].mean()
}

metrics_df = pd.DataFrame([metrics])

metrics_path.parent.mkdir(parents=True, exist_ok=True)

if metrics_path.exists():
    existing = pd.read_csv(metrics_path)
    metrics_df = pd.concat([existing, metrics_df], ignore_index=True)

metrics_df.to_csv(metrics_path, index=False)

print("Pipeline metrics recorded")