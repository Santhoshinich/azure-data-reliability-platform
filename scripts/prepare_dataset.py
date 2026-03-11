import pandas as pd
import uuid
import random
from datetime import datetime, timedelta

# Load raw dataset
df = pd.read_csv("../data/raw/creditcard.csv")

# Rename columns
df = df.rename(columns={
    "Amount": "amount",
    "Class": "fraud_label"
})

# Generate realistic fields
df["transaction_id"] = [str(uuid.uuid4()) for _ in range(len(df))]
df["customer_id"] = ["CUST_" + str(random.randint(1000, 9999)) for _ in range(len(df))]

# Simulate merchants
merchants = ["Amazon", "Walmart", "Target", "BestBuy", "Costco"]
df["merchant"] = [random.choice(merchants) for _ in range(len(df))]

# Simulate locations
locations = ["NY", "CA", "TX", "FL", "WA"]
df["location"] = [random.choice(locations) for _ in range(len(df))]

# Create timestamp
start_date = datetime(2023, 1, 1)
df["transaction_time"] = [
    start_date + timedelta(seconds=int(t))
    for t in df["Time"]
]

# Select useful columns
df = df[
    [
        "transaction_id",
        "customer_id",
        "transaction_time",
        "amount",
        "merchant",
        "location",
        "fraud_label"
    ]
]

# Save processed dataset
df.to_parquet("../data/bronze/transactions.parquet", index=False)

print("Bronze dataset created.")
print(df.head())