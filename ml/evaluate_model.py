from pathlib import Path
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

BASE_DIR = Path(__file__).resolve().parents[1]

data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"
model_path = BASE_DIR / "models" / "fraud_model.pkl"

df = pd.read_parquet(data_path)

model = joblib.load(model_path)

X = df[["amount"]]
y = df["fraud_label"]

preds = model.predict(X)

accuracy = accuracy_score(y, preds)

print("Model accuracy:", accuracy)

if accuracy < 0.7:
    raise Exception("Model accuracy below acceptable threshold")