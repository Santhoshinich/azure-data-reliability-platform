from pathlib import Path
import pandas as pd

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Build path to dataset
data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"

df = pd.read_parquet(data_path)

row_count = len(df)

expected_min = 200000
expected_max = 350000

print(f"Row count: {row_count}")

if row_count < expected_min or row_count > expected_max:
    raise Exception("Row count anomaly detected!")

print("Row count validation passed")