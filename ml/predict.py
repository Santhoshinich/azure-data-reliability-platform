from pathlib import Path
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parents[1]

data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"
model_path = BASE_DIR / "models" / "fraud_model.pkl"

df = pd.read_parquet(data_path)

model = joblib.load(model_path)

predictions = model.predict(df[["amount"]])

df["predicted_fraud"] = predictions

print("Predictions generated")