import os
import subprocess
import base64
import random
import math
from Pyfhel import Pyfhel  # Import Pyfhel library

# GitHub repository information
repo_directory = "repo"
file_path = "input.txt"
repo_url = "https://github.com/jayaf4u/home2.git"  # Replace with your repository URL

# Create a Pyfhel object
he = Pyfhel()  

# Generate keys
he.keyGen()

# Clone GitHub repository
subprocess.run(["git", "clone", repo_url, repo_directory], check=True)

# Read file content
with open(os.path.join(repo_directory, file_path), "r") as file:
    file_content = file.read()

# Encrypt file content using Pyfhel
encrypted_data = []
for char in file_content:
    encrypted_char = he.encryptInt(ord(char))
    encrypted_data.append(encrypted_char)

# Serialize encrypted data to bytes
serialized_data = b"".join([encrypted_char.to_bytes() for encrypted_char in encrypted_data])

# Save encrypted data to a file
encrypted_file_path = "encrypted_input.txt"
with open(encrypted_file_path, "wb") as encrypted_file:
    encrypted_file.write(base64.b64encode(serialized_data))

print("File encrypted and saved as", encrypted_file_path)
