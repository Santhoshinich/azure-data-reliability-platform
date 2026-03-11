\# Azure Data Reliability Platform



This project demonstrates how to build an automated \*\*data quality and validation framework\*\* for analytics pipelines and machine learning outputs.



The system simulates a financial transaction pipeline and validates data reliability using automated checks.



---



\## Project Goals



\- Validate data pipelines automatically

\- Detect data quality issues early

\- Implement schema and business rule validation

\- Monitor datasets used by analytics and ML models



---



\## Dataset



The project uses the \*\*Credit Card Fraud Detection dataset\*\* from Kaggle and transforms it into a realistic transaction dataset.



Dataset fields used:



transaction\_id  

customer\_id  

transaction\_time  

amount  

merchant  

location  

fraud\_label  



---



\## Data Architecture



The project follows a simplified \*\*medallion architecture\*\*:



Raw Data  

→ Bronze Layer (processed transaction dataset)  

→ Data Quality Validation  

→ Future Silver / Gold transformations



---



\## Data Quality Checks Implemented



\- Schema validation

\- Null value detection

\- Duplicate transaction detection

\- Business rule validation (amount > 0)



These checks are executed through a \*\*config-driven validation framework using YAML rules\*\*.



---



\## Project Structure

azure-data-reliability-platform/
data/
scripts/
data_quality/
config/




---

## Technologies Used

Python  
Pandas  
PyYAML  
Parquet  
Git

---

## Future Enhancements

- Data anomaly detection
- ML model validation
- CI/CD pipeline testing
- Data observability metrics

---

## How to Run

1. Prepare dataset

python scripts/prepare_dataset.py


2. Run data validation

python data_quality/validation_engine.py


---

## Author

Santhoshini Ch

Portfolio project demonstrating **data engineering and data reliability platform design**.




