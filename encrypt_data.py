from phe import paillier

# Load the input file
with open('input.txt', 'r') as file:
    data = file.read()

# Perform homomorphic encryption
public_key, private_key = paillier.generate_paillier_keypair()
encrypted_data = [public_key.encrypt(float(num)) for num in data.split()]

# Save the encrypted data to a new file
with open('encrypted_input.txt', 'w') as file:
    for encrypted_num in encrypted_data:
        file.write(str(encrypted_num) + '\n')
