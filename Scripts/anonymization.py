import pandas as pd
from db_connection import mydb

# Load from MySQL
covars = pd.read_sql('SELECT * FROM covars', mydb)
monitor = pd.read_sql('SELECT * FROM monitor', mydb)
customer = pd.read_csv('customers.csv', index_col="Unnamed: 0")

# Format date
def function(data):
    try:
        return pd.to_datetime(data, dayfirst=True).strftime('%Y-%m-%d')
    except (ValueError, TypeError):
        return data

customer['birthdate'] = customer['birthdate'].apply(function)
customer['birthdate'] = customer['birthdate'].str.replace('/', '-')
merged = covars.merge(monitor, on='mo_id').rename(columns={'dob': 'birthdate'})
merged2 = customer.merge(merged, on=['birthdate', 'sex'])

# Bin age
bins = [40, 45, 50, 55, 60]
merged2['age_group'] = pd.cut(merged2['age_recr'], bins, labels=["(40,45]", "(45,50]", "(50,55]", "(55,60]"])

cols = ['age_grouped', 'sex', 'area']
not_sens = pd.read_csv("Raw_information.csv", index_col="Index")
print('Uniquely Identifiable Individuals:', sum(not_sens.groupby(by=cols).size() == 1))

# Harmonize columns
def education_level_T(data):
    if data in ["bachelor", "masters", "phD", "other"]:
        return "higher education"
    elif data in ["secondary", "primary"]:
        return "non-higher education"

def ethnicity_T(data):
    asians = ["Pakistanti", "Indian", "Chinese", "Other Asian Background", "Bangladeshi"]
    blacks = ["Caribbean", "Other Black Background", "African", "White and Black African"]
    whites = ["White and Asian", "British", "Irish", "Other White Background"]
    if data in asians:
        return "Asian"
    elif data in blacks:
        return "Black"
    elif data in whites:
        return "White"
    return "Other"

not_sens["education_level"] = not_sens["education_level"].apply(education_level_T)
not_sens["Ethnicity"] = not_sens["Ethnicity"].apply(ethnicity_T)

# Filter by K-anonymity (k ≥ 2)
quasi_identifiers = ['age_grouped', 'area', 'sex', 'education_level', 'Ethnicity']
grouped = not_sens.groupby(quasi_identifiers)
anonymized_dataset = grouped.filter(lambda x: len(x) >= 2)

anonymized_dataset.to_csv('anonymized_information.csv')
