import os
import subprocess
import base64
import random
import math
import tenseal as ts  # Import TenSEAL library

# GitHub repository information
repo_directory = "repo"
file_path = "input.txt"
repo_url = "https://github.com/jayaf4u/home2.git"  # Replace with your repository URL

# Create a TenSEAL context
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=4096, coeff_mod_bit_sizes=[40, 40, 40, 40, 40])

# Generate public and secret keys
public_key, secret_key = context.keygen()

# Clone GitHub repository
subprocess.run(["git", "clone", repo_url, repo_directory], check=True)

# Read file content
with open(os.path.join(repo_directory, file_path), "r") as file:
    file_content = file.read()

# Encrypt file content using TenSEAL
encryptor = ts.Encryptor(context, public_key)
encrypted_data = []
for char in file_content:
    encrypted_char = encryptor.encrypt(ts.plain_tensor([ord(char)]))
    encrypted_data.append(encrypted_char)

# Serialize encrypted data to bytes
serialized_data = b"".join([encrypted_char.serialize() for encrypted_char in encrypted_data])

# Save encrypted data to a file
encrypted_file_path = "encrypted_input.txt"
with open(encrypted_file_path, "wb") as encrypted_file:
    encrypted_file.write(base64.b64encode(serialized_data))

print("File encrypted and saved as", encrypted_file_path)
