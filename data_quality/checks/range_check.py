def run_range_check(df, column, min_value):
    invalid = df[df[column] < min_value]

    if len(invalid) > 0:
        raise Exception(f"Range check failed for {column}: values below {min_value}")

    print(f"Range check passed for {column}")