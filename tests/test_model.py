from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parents[1]

model_path = BASE_DIR / "models" / "fraud_model.pkl"


def test_model_exists():

    assert model_path.exists()