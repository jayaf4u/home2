import os
import subprocess
import base64
import random
import math
import numpy as np
import seal  # Import PySEAL library

# GitHub repository information
repo_directory = "repo"
file_path = "input.txt"
repo_url = "https://github.com/jayaf4u/home2.git"  # Replace with your repository URL

# Create a SEAL context
parms = seal.EncryptionParameters(seal.SchemeType.BFV)
poly_modulus_degree = 4096
parms.set_poly_modulus_degree(poly_modulus_degree)
parms.set_coeff_modulus(seal.CoeffModulus.BFVDefault(poly_modulus_degree))
parms.set_plain_modulus(256)
context = seal.SEALContext.Create(parms)

# Generate public and secret keys
keygen = seal.KeyGenerator(context)
public_key = keygen.public_key()
secret_key = keygen.secret_key()

# Clone GitHub repository
subprocess.run(["git", "clone", repo_url, repo_directory], check=True)

# Read file content
with open(os.path.join(repo_directory, file_path), "r") as file:
    file_content = file.read()

# Encrypt file content using PySEAL
encryptor = seal.Encryptor(context, public_key)
encrypted_data = []
for char in file_content:
    plaintext = seal.Plaintext(str(ord(char)))
    encrypted_char = seal.Ciphertext()
    encryptor.encrypt(plaintext, encrypted_char)
    encrypted_data.append(encrypted_char)

# Serialize encrypted data to bytes
serialized_data = b"".join([encrypted_char.save() for encrypted_char in encrypted_data])

# Save encrypted data to a file
encrypted_file_path = "encrypted_input.txt"
with open(encrypted_file_path, "wb") as encrypted_file:
    encrypted_file.write(base64.b64encode(serialized_data))

print("File encrypted and saved as", encrypted_file_path)
