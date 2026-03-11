import pandas as pd
import yaml

from checks.null_check import run_null_check
from checks.duplicate_check import run_duplicate_check
from checks.range_check import run_range_check
from checks.schema_check import run_schema_check


def run_validation():

    df = pd.read_parquet("../data/bronze/transactions.parquet")

    with open("rules/transaction_rules.yaml") as f:
        rules = yaml.safe_load(f)

    with open("../config/schema_contract.yaml") as f:
        schema_config = yaml.safe_load(f)

    # Run schema validation first
    run_schema_check(df, schema_config["schema"])

    # Run rule-based checks
    for check in rules["checks"]:

        if check["type"] == "null_check":
            run_null_check(df, check["column"])

        if check["type"] == "duplicate_check":
            run_duplicate_check(df, check["column"])

        if check["type"] == "range_check":
            run_range_check(df, check["column"], check["min"])

    print("\nAll data quality checks passed!")


if __name__ == "__main__":
    run_validation()