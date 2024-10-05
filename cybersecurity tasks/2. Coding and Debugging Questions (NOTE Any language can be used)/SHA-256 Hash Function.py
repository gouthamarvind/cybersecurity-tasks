import hashlib

def hash_password(password):
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the password bytes
    sha256_hash.update(password_bytes)
    # Return the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

# Get password input from the user
user_password = input("Enter your password: ")

# Get the SHA-256 hash of the password
hashed_password = hash_password(user_password)

# Print the hashed password
print(f"SHA-256 hash of the password: {hashed_password}")
