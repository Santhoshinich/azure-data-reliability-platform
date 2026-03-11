def run_schema_check(df, expected_schema):

    actual_schema = dict(df.dtypes)

    for column, dtype in expected_schema.items():

        if column not in actual_schema:
            raise Exception(f"Schema check failed: Missing column {column}")

        if str(actual_schema[column]) != dtype:
            raise Exception(
                f"Schema check failed for {column}: expected {dtype}, got {actual_schema[column]}"
            )

    print("Schema validation passed")