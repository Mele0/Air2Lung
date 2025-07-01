# Lung Disease Cohort Analysis

This project focuses on constructing, querying, analyzing, and securing a relational database for a simulated clinical study. The study investigates associations between air pollution, lifestyle factors, and lung disease among 1,000 UK participants. The project integrates SQL (MySQL), Python, data privacy techniques, and encryption.

## 🧪 Project Objectives

- Create a MySQL database and import cohort data from multiple CSV sources.
- Explore demographic and exposure variables using SQL queries.
- Assess air quality exposure and its relation to disease status.
- Implement privacy-preserving techniques including k-anonymity and encryption.
- Use Python to query the database and manipulate patient-level data.

## 📁 Dataset Description

The project uses a synthetic cohort study consisting of:

- **covars.csv**: Demographic and clinical data including sex, age at recruitment, disease status, smoking data, etc.
- **monitor.csv**: Environmental exposure data at monitoring sites (PM2.5, NO2).
- **customers.csv**: Insurance records including personal identifiers and lifestyle factors.

## ⚙️ Tools and Technologies

- **SQL**: MySQL 8.0, DBeaver
- **Python**: `pandas`, `sqlalchemy`, `mysql-connector-python`, `cryptography`
- **Environment**: Jupyter Notebook, VSCode

## 🔍 Key Features

### 1. Database Construction
MySQL scripts build a relational database `lung_disease_DB` with foreign key relations and correct datatypes, enabling clean integration of environmental and participant-level data.

### 2. Data Analysis (SQL)
Queries assess cohort characteristics:
- Age distribution
- Disease prevalence across regions
- Environmental exposure (PM2.5, NO2)
- Smoking intensity (Pack Years)

Views and updated schema elements (e.g., `pack_years`) were added to support repeated queries and visualization.

### 3. Python Integration
Python scripts:
- Establish secure connection to the MySQL database
- Extract and manipulate cohort subsets
- Validate SQL queries within a Python data science pipeline

### 4. Data Privacy & Anonymization

#### HIPAA-Informed Classification:
- **Sensitive Identifiers**: Name, phone number, bank details
- **Quasi-identifiers**: Age group, sex, ethnicity, education level, area

Data split into two linked CSVs:
- `Sensitive_information.csv`
- `Raw_information.csv`

A re-identification risk assessment showed **83 individuals** could be uniquely identified using just quasi-identifiers—highlighting the insufficiency of basic de-identification.

---

#### 🧠 Mondrian Method for K-Anonymity

To anonymize quasi-identifiers in our dataset, we used a custom binning and generalization strategy inspired by the **Mondrian multidimensional k-anonymity** algorithm.

The Mondrian method recursively partitions data into multidimensional regions until no further division is possible without violating the desired k-anonymity threshold. It balances privacy and data utility by minimizing information loss.

For more details, refer to the [original paper](https://pages.cs.wisc.edu/~lefevre/MultiDim.pdf).

<div align="center">
  <img src="https://frontdesk.co.in/wp-content/uploads/2024/05/image-15.png" width="400"/>
  <p><em>Figure: A simplified illustration of Mondrian partitioning in two dimensions.</em></p>
</div>

---

#### K-Anonymity Strategy:
Using the Mondrian-inspired approach, we achieved:

| K-Anonymity Level | Samples Retained |
|-------------------|------------------|
| ≥1                | 1000             |
| ≥2                | 367              |
| ≥3                | 109              |
| ≥4                | 16               |

Final anonymized dataset: `Anonymized_information.csv`

### 5. Data Encryption

Used the `cryptography` Python package and Fernet symmetric encryption to securely encrypt anonymized datasets. Decryption requires the private key shared separately.

```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
# Encrypt
encrypted = f.encrypt(b"your_data_here")
# Decrypt
decrypted = f.decrypt(encrypted)
