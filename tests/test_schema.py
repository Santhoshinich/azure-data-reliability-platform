from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"

expected_columns = [
    "transaction_id",
    "customer_id",
    "transaction_time",
    "amount",
    "merchant",
    "location",
    "fraud_label"
]


def test_schema():

    df = pd.read_parquet(data_path)

    for column in expected_columns:
        assert column in df.columns