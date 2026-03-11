def run_duplicate_check(df, column):
    duplicate_count = df[column].duplicated().sum()

    if duplicate_count > 0:
        raise Exception(f"Duplicate check failed for {column}: {duplicate_count} duplicates")

    print(f"Duplicate check passed for {column}")