# Azure Data Reliability Platform



This project demonstrates how to build an automated \*\*data quality and validation framework\*\* for analytics pipelines and machine learning outputs.



The system simulates a financial transaction pipeline and validates data reliability using automated checks.



---



## Project Goals



\- Validate data pipelines automatically

\- Detect data quality issues early

\- Implement schema and business rule validation

\- Monitor datasets used by analytics and ML models



---



## Dataset



The project uses the \*\*Credit Card Fraud Detection dataset\*\* from Kaggle and transforms it into a realistic transaction dataset.



Dataset fields used:



\- transaction_id  

\- customer_id  

\- transaction_time  

\- amount  

\- merchant  

\- location  

\- fraud_label  



---



## Data Architecture



The project follows a simplified \*\*medallion architecture\*\*:



Raw Data  

→ Bronze Layer (processed transaction dataset)  

→ Data Quality Validation  

→ Future Silver / Gold transformations



---



## Data Quality Checks Implemented



\- Schema validation

\- Null value detection

\- Duplicate transaction detection

\- Business rule validation (amount > 0)



These checks are executed through a \*\*config-driven validation framework using YAML rules\*\*.



---



## Repo Structure

azure-data-reliability-platform/

scripts/
    prepare_dataset.py

data_quality/
    validation_engine.py
    checks/
    rules/

monitoring/
    row_count_monitor.py

config/
    schema_contract.yaml

README.md
requirements.txt
.gitignore



---

## Technologies Used

\- Python 
 
\- Pandas
  
\- PyYAML
  
\- Parquet
  
\- Git

---

## Future Enhancements

\- Data anomaly detection

\- ML model validation

\- CI/CD pipeline testing

\- Data observability metrics

---

## How to Run

1. Prepare dataset

python scripts/prepare_dataset.py


2. Run data validation

python data_quality/validation_engine.py

3. Run monitoring row count

python monitoring/row_count_monitor.py



---

## Author

Santhoshini Ch

Portfolio project demonstrating **Data engineering and data reliability platform design**.




