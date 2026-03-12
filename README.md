# Azure Data Reliability & ML Validation Platform

## Overview

This project demonstrates how to build a **data reliability and machine learning validation platform** for analytics pipelines.

The system simulates a financial transaction pipeline where data is:

1. Ingested and transformed
2. Validated using automated data quality checks
3. Monitored for anomalies and distribution drift
4. Used to train a fraud detection ML model
5. Tested automatically through a CI pipeline

The goal of this project is to demonstrate **modern data engineering, data reliability, and MLOps practices** used in production data platforms.

---

# Problem This Project Solves

Modern data platforms frequently break due to:

* schema changes in source systems
* corrupted or incomplete datasets
* pipeline failures
* distribution drift in ML features
* model performance degradation

Without automated checks, these problems propagate into:

* dashboards
* analytics reports
* machine learning predictions
* financial systems

This project demonstrates how a **data reliability platform can detect these problems automatically before they impact downstream systems.**

---

# System Architecture

The platform simulates a modern **data + ML reliability architecture**.

```
Git Push
   ↓
CI Pipeline (GitHub Actions)
   ↓
Dataset Preparation
   ↓
Data Quality Validation
   ↓
Observability Monitoring
   ↓
Distribution Drift Detection
   ↓
Pipeline Metrics Collection
   ↓
Machine Learning Model Training
   ↓
Model Evaluation
   ↓
Automated Tests
```

---

# Detailed Architecture

```
                   +----------------------+
                   |     Git Push         |
                   +----------+-----------+
                              |
                              v
                +----------------------------+
                | CI Pipeline (GitHub)       |
                | GitHub Actions Runner      |
                +------------+---------------+
                             |
                             v
                +----------------------------+
                | Dataset Preparation        |
                | scripts/prepare_dataset.py |
                +------------+---------------+
                             |
                             v
                +----------------------------+
                | Data Quality Validation    |
                | validation_engine.py       |
                |                            |
                | • schema validation        |
                | • null checks              |
                | • duplicate detection      |
                | • business rules           |
                +------------+---------------+
                             |
                             v
                +----------------------------+
                | Data Observability         |
                |                            |
                | row_count_monitor.py       |
                | data_drift_monitor.py      |
                | distribution_drift_monitor |
                +------------+---------------+
                             |
                             v
                +----------------------------+
                | Pipeline Metrics Tracking  |
                | pipeline_metrics.py        |
                +------------+---------------+
                             |
                             v
                +----------------------------+
                | Machine Learning Pipeline  |
                |                            |
                | train_model.py             |
                | predict.py                 |
                | evaluate_model.py          |
                +------------+---------------+
                             |
                             v
                +----------------------------+
                | Automated Tests (pytest)   |
                +----------------------------+
```

---

# Key Components

## 1. Data Pipeline

The pipeline converts raw transaction data into a structured analytics dataset.

Script

```
scripts/prepare_dataset.py
```

Functions

* load raw dataset
* transform columns
* generate transaction metadata
* convert dataset to parquet format
* store dataset in bronze layer

Output dataset

```
data/bronze/transactions.parquet
```

---

# 2. Data Quality Framework

A configurable validation engine performs automated checks on the dataset.

Script

```
data_quality/validation_engine.py
```

Checks implemented

* schema validation
* null value detection
* duplicate detection
* business rule validation

Validation rules

```
data_quality/rules/transaction_rules.yaml
```

Schema contract

```
config/schema_contract.yaml
```

---

# 3. Data Observability Monitoring

Monitoring scripts detect unexpected data behavior.

Monitoring modules

```
monitoring/
    row_count_monitor.py
    data_drift_monitor.py
    distribution_drift_monitor.py
```

These checks detect

* abnormal row counts
* unexpected fraud rate changes
* distribution drift in transaction amounts

---

# 4. Distribution Drift Detection

The project implements **statistical drift detection** using the Kolmogorov–Smirnov test.

Purpose

Compare the distribution of current data with a baseline dataset to detect feature drift.

Script

```
monitoring/distribution_drift_monitor.py
```

If drift is detected, the pipeline automatically fails.

---

# 5. Pipeline Metrics Tracking

Each pipeline run records operational metrics.

Script

```
monitoring/pipeline_metrics.py
```

Metrics collected

* row count
* average transaction amount
* fraud rate
* pipeline run timestamp

Metrics stored in

```
metrics/pipeline_metrics.csv
```

These metrics can be used to build monitoring dashboards.

---

# 6. Machine Learning Pipeline

The project includes a fraud detection model trained on transaction data.

ML module

```
ml/
```

Components

| File              | Purpose                      |
| ----------------- | ---------------------------- |
| train_model.py    | trains fraud detection model |
| predict.py        | generates predictions        |
| evaluate_model.py | validates model performance  |

Model artifact

```
models/fraud_model.pkl
```

The pipeline verifies that model accuracy meets a minimum threshold.

---

# 7. Automated Testing

Automated tests ensure pipeline reliability.

Testing framework

```
pytest
```

Test files

```
tests/
    test_schema.py
    test_business_rules.py
    test_row_count.py
    test_model.py
```

These tests validate

* schema integrity
* business rule compliance
* dataset size expectations
* ML model artifacts

Example test output

```
tests/test_business_rules.py ..
tests/test_model.py .
tests/test_row_count.py .
tests/test_schema.py .

5 passed
```

---

# 8. Continuous Integration Pipeline

The repository contains a CI pipeline using GitHub Actions.

Workflow

```
.github/workflows/data_validation.yml
```

Pipeline steps

1. Install dependencies
2. Download dataset
3. Prepare dataset
4. Run data validation checks
5. Run monitoring checks
6. Run drift detection
7. Record pipeline metrics
8. Train ML model
9. Evaluate model
10. Run automated tests

If any step fails, the pipeline stops automatically.

---

9. ## Observability Dashboard

Dashboard built using:

Streamlit

File:

```
dashboard/metrics_dashboard.py
```

Features:

* pipeline health indicators
* data trend charts
* fraud rate monitoring
* metrics history
* custom styling and gradient background
* author branding (Santhoshini Ch)

Run dashboard:

python -m streamlit run dashboard/metrics_dashboard.py

---

# Technologies Used

### Data Processing

* Python
* Pandas
* PyArrow

### Machine Learning

* scikit-learn
* joblib

### Statistical Testing

* SciPy

### Testing

* pytest

### Automation

* GitHub Actions

### Dashboard

* streamlit

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

dashboard/
    metrics_dashboard.py

monitoring/
    row_count_monitor.py
    data_drift_monitor.py
    distribution_drift_monitor.py
    pipeline_metrics.py

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

metrics/
    pipeline_metrics.csv

models/

data/

.github/
    workflows/
```

---

# Running the Project Locally

Install dependencies

```
pip install -r requirements.txt
```

Prepare dataset

```
python scripts/prepare_dataset.py
```

Run validation checks

```
python data_quality/validation_engine.py
```

Run monitoring checks

```
python monitoring/row_count_monitor.py
```

Run drift detection

```
python monitoring/distribution_drift_monitor.py
```

Record pipeline metrics

```
python monitoring/pipeline_metrics.py
```

Train ML model

```
python ml/train_model.py
```

Run tests

```
pytest
```

---

# Future Enhancements

Planned improvements include

* Azure pipeline orchestration
* experiment tracking for ML models
* feature store simulation
* alerting for pipeline failures
* data lineage tracking

---

# What This Project Demonstrates

This project demonstrates skills across multiple engineering domains.

| Area                 | Capability            |
| -------------------- | --------------------- |
| Data Engineering     | pipeline design       |
| Data Reliability     | validation framework  |
| Data Observability   | anomaly monitoring    |
| MLOps                | drift detection       |
| Machine Learning     | fraud detection model |
| Software Engineering | automated testing     |
| DevOps               | CI automation         |

---

# Author

Santhoshini Ch

Data Engineering & Data Reliability Portfolio Project

Demonstrates experience in:

* data pipeline engineering
* data quality validation
* observability monitoring
* machine learning validation
* CI/CD automation
* observability dashboard for pipeline metrics

# Resume Summary

This project simulates a **modern data reliability platform** that validates data pipelines, monitors anomalies and drift, trains ML models, tracks metrics, and visualizes pipeline health through an observability dashboard.
