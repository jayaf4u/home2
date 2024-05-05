import os
from github import Github
from pypaillier import paillier
import base64

# GitHub repository information
github_username = "jayaf4u"
github_token = "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"  # Generate a personal access token from GitHub
repo_name = "home2"
file_path = "input.txt"

# Connect to GitHub
g = Github(github_token)
repo = g.get_user(github_username).get_repo(repo_name)

# Fetch file content from GitHub
file_content = repo.get_contents(file_path).decoded_content.decode()

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
