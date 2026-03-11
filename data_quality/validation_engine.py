from pathlib import Path
import pandas as pd
import yaml

from checks.null_check import run_null_check
from checks.duplicate_check import run_duplicate_check
from checks.range_check import run_range_check
from checks.schema_check import run_schema_check

BASE_DIR = Path(__file__).resolve().parent.parent

data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"
rules_path = BASE_DIR / "data_quality" / "rules" / "transaction_rules.yaml"
schema_path = BASE_DIR / "config" / "schema_contract.yaml"


def run_validation():

    df = pd.read_parquet(data_path)

    with open(rules_path) as f:
        rules = yaml.safe_load(f)

    with open(schema_path) as f:
        schema_config = yaml.safe_load(f)

    run_schema_check(df, schema_config["schema"])

    for check in rules["checks"]:

        if check["type"] == "null_check":
            run_null_check(df, check["column"])

        elif check["type"] == "duplicate_check":
            run_duplicate_check(df, check["column"])

        elif check["type"] == "range_check":
            run_range_check(df, check["column"], check["min"])

    print("\nAll data quality checks passed")


if __name__ == "__main__":
    run_validation()