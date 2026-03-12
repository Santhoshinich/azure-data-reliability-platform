# Azure Data Reliability & ML Validation Platform

## Overview

This project demonstrates how to build a **data reliability and machine learning validation platform** for analytics pipelines.
It simulates a financial transaction system where data is ingested, validated, monitored for anomalies, used to train a fraud detection model, and automatically tested through a CI pipeline.

The goal of this project is to showcase **modern data engineering practices**, including:

* automated data quality validation
* data observability monitoring
* machine learning model validation
* automated testing
* CI pipeline automation

This project is designed as a **portfolio demonstration of data reliability engineering concepts used in production data platforms.**

---

# Problem This Project Solves

Modern data platforms frequently fail due to issues such as:

* upstream data pipeline failures
* schema changes in source systems
* corrupted datasets
* unexpected data anomalies
* machine learning model degradation

Without automated validation, these problems can propagate into:

* dashboards
* analytics reports
* machine learning predictions
* financial systems

This project demonstrates how a **data reliability system can automatically detect these problems before they impact downstream systems.**

---

# Architecture

The platform simulates a modern **data + ML reliability pipeline**.

```text
                   +--------------------+
                   |  Raw Dataset (CSV) |
                   +--------------------+
                             |
                             v
                   +--------------------+
                   | Data Preparation   |
                   | prepare_dataset.py |
                   +--------------------+
                             |
                             v
                   +--------------------+
                   | Data Validation    |
                   | validation_engine  |
                   +--------------------+
                             |
                             v
                   +--------------------+
                   | Observability      |
                   | row_count_monitor  |
                   +--------------------+
                             |
                             v
                   +--------------------+
                   | ML Training        |
                   | train_model.py     |
                   +--------------------+
                             |
                             v
                   +--------------------+
                   | Model Evaluation   |
                   | evaluate_model.py  |
                   +--------------------+
                             |
                             v
                   +--------------------+
                   | Automated Tests    |
                   | pytest             |
                   +--------------------+
                             |
                             v
                   +--------------------+
                   | CI Pipeline        |
                   | GitHub Actions     |
                   +--------------------+
```

---

# Key Features

## 1. Data Pipeline

The pipeline converts raw transaction data into a structured analytics dataset.

Script:

```
scripts/prepare_dataset.py
```

Functions performed:

* load raw transaction dataset
* transform fields
* generate synthetic metadata
* convert dataset to parquet format
* store dataset in the Bronze data layer

Output dataset:

```
data/bronze/transactions.parquet
```

---

# 2. Data Quality Validation Framework

The project implements a configurable **data validation engine**.

Validation script:

```
data_quality/validation_engine.py
```

Checks implemented:

* schema validation
* null value detection
* duplicate transaction detection
* range validation for business rules

Validation rules are defined in:

```
data_quality/rules/transaction_rules.yaml
```

Schema contract:

```
config/schema_contract.yaml
```

---

# 3. Data Observability Monitoring

Monitoring scripts detect abnormal data behavior.

Example monitor:

```
monitoring/row_count_monitor.py
```

Current monitoring checks:

* dataset row count anomaly detection
* pipeline integrity validation

These checks simulate features typically found in **data observability platforms**.

---

# 4. Machine Learning Pipeline

The project includes a **fraud detection model** trained on the transaction dataset.

ML module:

```
ml/
```

Components:

| File              | Purpose                      |
| ----------------- | ---------------------------- |
| train_model.py    | trains fraud detection model |
| predict.py        | generates fraud predictions  |
| evaluate_model.py | validates model performance  |

Model artifact:

```
models/fraud_model.pkl
```

The pipeline automatically verifies that the trained model meets a minimum accuracy threshold.

---

# 5. Automated Testing

The project includes automated tests using pytest.

Testing framework: **pytest**

Test files:

```
tests/test_schema.py
tests/test_business_rules.py
tests/test_row_count.py
tests/test_model.py
```

These tests verify:

* dataset schema integrity
* business rule compliance
* dataset size expectations
* ML model artifacts

Example test output:

```
============================= test session starts ==============================

tests/test_business_rules.py ..
tests/test_model.py .
tests/test_row_count.py .
tests/test_schema.py .

========================= 5 passed =========================
```

---

# 6. Continuous Integration Pipeline

The repository contains a CI pipeline implemented using GitHub Actions.

Workflow file:

```
.github/workflows/data_validation.yml
```

Pipeline steps:

1. Install dependencies
2. Download dataset
3. Prepare dataset
4. Run data validation checks
5. Run monitoring checks
6. Train ML model
7. Evaluate model performance
8. Execute automated tests

Example CI run:

```
Prepare dataset ✔
Run validation ✔
Monitoring checks ✔
Train ML model ✔
Evaluate model ✔
Run pytest tests ✔
```

If any step fails, the pipeline stops automatically.

---

# Technologies Used

**Data Processing**

* Python
* Pandas
* PyArrow

**Machine Learning**

* scikit-learn
* joblib

**Testing**

* pytest

**Automation**

* GitHub Actions

---

# Project Structure

```
azure-data-reliability-platform/

scripts/
    prepare_dataset.py

data_quality/
    validation_engine.py
    checks/
    rules/

monitoring/
    row_count_monitor.py

ml/
    train_model.py
    predict.py
    evaluate_model.py

tests/
    test_schema.py
    test_business_rules.py
    test_row_count.py
    test_model.py

config/
    schema_contract.yaml

models/

data/

.github/
    workflows/
```

---

# Running the Project Locally

Install dependencies:

```
pip install -r requirements.txt
```

Prepare dataset:

```
python scripts/prepare_dataset.py
```

Run validation checks:

```
python data_quality/validation_engine.py
```

Run monitoring checks:

```
python monitoring/row_count_monitor.py
```

Train ML model:

```
python ml/train_model.py
```

Run automated tests:

```
pytest
```

---

# Example Pipeline Flow

```
Git Push
   ↓
GitHub Actions Runner
   ↓
Dataset Preparation
   ↓
Data Validation
   ↓
Monitoring Checks
   ↓
ML Model Training
   ↓
Model Evaluation
   ↓
Automated Tests
```

---

# Project Walkthrough (Interview Explanation)

This project simulates a **data reliability platform used in modern analytics and ML systems**.

The system processes transaction data through a pipeline that performs:

* data preparation
* automated validation
* anomaly monitoring
* machine learning model training
* automated testing

The pipeline is designed to **prevent unreliable data from propagating into analytics systems or ML models.**

### Key Design Decisions

**Data Quality Framework**

A rule-based validation system ensures:

* required columns exist
* null values are detected
* duplicate transactions are flagged
* business rules are enforced

Validation logic is configurable through YAML rules.

---

**Data Observability**

Monitoring scripts detect abnormal dataset behavior such as row-count anomalies.

---

**Machine Learning Validation**

A fraud detection model is trained on transaction data.
The pipeline verifies model performance before allowing the pipeline to complete.

---

**Automated Testing**

Pytest ensures reliability of:

* dataset schema
* business rules
* dataset size
* ML artifacts

---

**Continuous Integration**

GitHub Actions automatically validates the entire pipeline whenever code changes occur.

---

# Future Improvements

Possible enhancements include:

* feature drift detection
* model drift monitoring
* data lineage tracking
* Azure pipeline orchestration
* experiment tracking for ML models

---


# Author

Data Engineering & Data Reliability Portfolio Project

This project demonstrates experience in:

* data pipeline engineering
* data quality validation
* observability monitoring
* machine learning validation
* CI/CD automation
