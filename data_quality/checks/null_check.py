def run_null_check(df, column):
    null_count = df[column].isnull().sum()

    if null_count > 0:
        raise Exception(f"Null check failed for {column}: {null_count} null values")

    print(f"Null check passed for {column}")