import os
import subprocess
import base64
import random
import math
from pyseal import CKKS, Encryptor, SecretKey, PublicKey

# GitHub repository information
repo_directory = "repo"
file_path = "input.txt"
repo_url = "https://github.com/jayaf4u/home2.git"  # Replace with your repository URL

# Create PySEAL context
context = CKKS()

# Generate public and secret keys
public_key = PublicKey()
secret_key = SecretKey()
public_key.load(context, "path_to_public_key_file")  # Replace "path_to_public_key_file" with the actual path
secret_key.load(context, "path_to_secret_key_file")  # Replace "path_to_secret_key_file" with the actual path

# Clone GitHub repository
subprocess.run(["git", "clone", repo_url, repo_directory], check=True)

# Read file content
with open(os.path.join(repo_directory, file_path), "r") as file:
    file_content = file.read()

# Encrypt file content using PySEAL
encryptor = Encryptor(context, public_key)
encrypted_data = []
for char in file_content:
    encrypted_char = encryptor.encrypt(context.encode_char(char))
    encrypted_data.append(encrypted_char)

# Serialize encrypted data to bytes
serialized_data = b"".join([encrypted_char.serialize() for encrypted_char in encrypted_data])

# Save encrypted data to a file
encrypted_file_path = "encrypted_input.txt"
with open(encrypted_file_path, "wb") as encrypted_file:
    encrypted_file.write(base64.b64encode(serialized_data))

print("File encrypted and saved as", encrypted_file_path)
