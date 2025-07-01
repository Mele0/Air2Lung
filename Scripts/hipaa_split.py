import pandas as pd

# Load dataset
customer = pd.read_csv('customers.csv', index_col="Unnamed: 0")

# Define identifiers
sensitive_cols = ['given_name', 'surname', 'birthdate', 'phone_number', 'national_insurance_number', 'bank_account_number', 'IP_Address', 'postcode']
quasi_cols = ['sex', 'age_grouped', 'Ethnicity', 'education_level', 'area', 'current_country', 'Chip_ID']

# Split datasets
not_sensitive = [col for col in customer.columns if col not in sensitive_cols]
sensitive = customer[sensitive_cols]
not_sens = customer[not_sensitive]

# Save subsets
sensitive.to_csv('Sensitive_information.csv', index=True, index_label="Index")
not_sens.to_csv('Raw_information.csv', index=True, index_label="Index")
