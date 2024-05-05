import os
import subprocess
import base64
import random
import math

# Generate a pair of large prime numbers
def generate_large_primes():
    # Replace these with actual prime number generation algorithms
    # For demonstration, we generate small primes here
    p = 17
    q = 19
    return p, q

# Calculate the least common multiple
def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

# Generate public and private keys
def generate_keys():
    p, q = generate_large_primes()
    n = p * q
    phi = lcm(p - 1, q - 1)

    # Choose a random integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Compute d, the modular multiplicative inverse of e modulo phi
    d = pow(e, -1, phi)

    return (e, n), (d, n)

# Encrypt a message using the public key
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [(char ** e) % n for char in message]
    return encrypted_message

# Decrypt a message using the private key
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [(char ** d) % n for char in encrypted_message]
    return decrypted_message

# GitHub repository information
repo_directory = "repo"
file_path = "input.txt"
repo_url = "https://github.com/jayaf4u/home2.git"  # Replace with your repository URL

# Clone GitHub repository
subprocess.run(["git", "clone", repo_url, repo_directory], check=True)

# Read file content
with open(os.path.join(repo_directory, file_path), "r") as file:
    file_content = file.read()

# Convert file content to list of ASCII values
ascii_values = [ord(char) for char in file_content]

# Generate public and private keys
public_key, private_key = generate_keys()

# Encrypt file content
encrypted_data = encrypt(ascii_values, public_key)

# Save encrypted data to a file
encrypted_file_path = "encrypted_input.txt"
with open(encrypted_file_path, "w") as encrypted_file:
    encrypted_file.write(base64.b64encode(bytes(encrypted_data)).decode())

print("File encrypted and saved as", encrypted_file_path)
