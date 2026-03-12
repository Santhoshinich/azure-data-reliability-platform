from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

BASE_DIR = Path(__file__).resolve().parents[1]

data_path = BASE_DIR / "data" / "bronze" / "transactions.parquet"
model_path = BASE_DIR / "models" / "fraud_model.pkl"

df = pd.read_parquet(data_path)

# simple feature selection
X = df[["amount"]]
y = df["fraud_label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()

model.fit(X_train, y_train)

model_path.parent.mkdir(parents=True, exist_ok=True)

joblib.dump(model, model_path)

print("Model trained and saved")