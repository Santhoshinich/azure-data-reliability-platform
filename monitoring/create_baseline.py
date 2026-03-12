from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"
baseline_path = BASE_DIR / "monitoring" / "baseline" / "baseline_transactions.parquet"

df = pd.read_parquet(data_path)

baseline_path.parent.mkdir(parents=True, exist_ok=True)

df.to_parquet(baseline_path)

print("Baseline dataset created")