from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"

df = pd.read_parquet(data_path)

avg_amount = df["amount"].mean()
fraud_rate = df["fraud_label"].mean()

print("Average transaction amount:", avg_amount)
print("Fraud rate:", fraud_rate)

# baseline expectations
baseline_amount = 90
baseline_fraud_rate = 0.002

if abs(avg_amount - baseline_amount) > 200:
    raise Exception("Transaction amount drift detected")

if abs(fraud_rate - baseline_fraud_rate) > 0.02:
    raise Exception("Fraud rate drift detected")

print("No data drift detected")