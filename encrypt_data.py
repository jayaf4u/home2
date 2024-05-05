import os
from pypaillier import paillier
import base64

# GitHub repository information
repo_directory = "repo"
file_path = "input.txt"
repo_url = "https://github.com/jayaf4u/home2.git"  # Replace with your repository URL

# Clone GitHub repository
os.system(f"git clone {repo_url} {repo_directory}")

# Read file content
with open(os.path.join(repo_directory, file_path), "r") as file:
    file_content = file.read()

# Perform Paillier encryption
public_key, private_key = paillier.generate_paillier_keypair()

# Encrypt file content
encrypted_data = []
for char in file_content:
    encrypted_char = public_key.encrypt(ord(char))
    encrypted_data.append(encrypted_char)

# Save encrypted data to a file
encrypted_file_path = "encrypted_input.txt"
with open(encrypted_file_path, "w") as encrypted_file:
    encrypted_file.write(base64.b64encode(bytes(encrypted_data)).decode())

print("File encrypted and saved as", encrypted_file_path)
