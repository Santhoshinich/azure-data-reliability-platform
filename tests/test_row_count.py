from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"


def test_row_count():

    df = pd.read_parquet(data_path)

    # dataset should not be unexpectedly small
    assert len(df) > 200000