def run_schema_check(df, expected_schema):

    actual_schema = dict(df.dtypes)

    for column, expected_dtype in expected_schema.items():

        if column not in actual_schema:
            raise Exception(f"Schema check failed: Missing column {column}")

        actual_dtype = str(actual_schema[column])

        # Handle string types
        if expected_dtype in ["object", "str"] and actual_dtype in ["object", "string", "str"]:
            continue

        # Handle datetime precision differences
        if expected_dtype.startswith("datetime64") and actual_dtype.startswith("datetime64"):
            continue

        if actual_dtype != expected_dtype:
            raise Exception(
                f"Schema check failed for {column}: expected {expected_dtype}, got {actual_dtype}"
            )

    print("Schema validation passed")