from pathlib import Path
import pandas as pd
from scipy.stats import ks_2samp

BASE_DIR = Path(__file__).resolve().parents[1]

current_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"
baseline_path = BASE_DIR / "monitoring" / "baseline" / "baseline_transactions.parquet"

current_df = pd.read_parquet(current_path)
baseline_df = pd.read_parquet(baseline_path)

# Compare distributions
stat, p_value = ks_2samp(
    baseline_df["amount"],
    current_df["amount"]
)

print("KS Statistic:", stat)
print("P-value:", p_value)

if p_value < 0.05:
    raise Exception("Distribution drift detected in transaction amounts")

print("No distribution drift detected")