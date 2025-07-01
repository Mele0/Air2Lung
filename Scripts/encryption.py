from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()
f = Fernet(key)

# Encrypt
filename_NE = 'anonymized_information.csv'
filename_E = 'anonymized_information_Encrypted.csv'

with open(filename_NE, "rb") as file:
    file_data = file.read()
    encrypted_data = f.encrypt(file_data)

with open(filename_E, "wb") as file:
    file.write(encrypted_data)

# Decrypt
with open(filename_E, "rb") as file:
    encrypted_data = file.read()

decrypted_data = f.decrypt(encrypted_data)
with open(filename_NE, "wb") as file:
    file.write(decrypted_data)
