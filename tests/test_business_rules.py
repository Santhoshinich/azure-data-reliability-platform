from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"


def test_amount_non_negative():

    df = pd.read_parquet(data_path)

    # business rule: amount cannot be negative
    assert (df["amount"] >= 0).all()


def test_no_null_transaction_id():

    df = pd.read_parquet(data_path)

    assert df["transaction_id"].isnull().sum() == 0