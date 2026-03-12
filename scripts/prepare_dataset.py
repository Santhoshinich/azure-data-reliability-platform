from pathlib import Path
import pandas as pd
import uuid
import random
from datetime import datetime, timedelta

# Resolve project root
BASE_DIR = Path(__file__).resolve().parent.parent

raw_path = BASE_DIR / "data" / "raw" / "creditcard.csv"
bronze_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"

# Load dataset
df = pd.read_csv(raw_path)

df = df.rename(columns={
    "Amount": "amount",
    "Class": "fraud_label"
})

# Generate additional columns
df["transaction_id"] = [str(uuid.uuid4()) for _ in range(len(df))]
df["customer_id"] = ["CUST_" + str(random.randint(1000,9999)) for _ in range(len(df))]

merchants = ["Amazon","Walmart","Target","Costco","BestBuy"]
df["merchant"] = [random.choice(merchants) for _ in range(len(df))]

locations = ["NY","CA","TX","WA","FL"]
df["location"] = [random.choice(locations) for _ in range(len(df))]

start_date = datetime(2023,1,1)

df["transaction_time"] = [
    start_date + timedelta(seconds=int(t))
    for t in df["Time"]
]

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

bronze_path.parent.mkdir(parents=True, exist_ok=True)

# Save bronze dataset
df.to_parquet(bronze_path,index=False)

print("Bronze dataset created")
print(f"Saved to: {bronze_path}")