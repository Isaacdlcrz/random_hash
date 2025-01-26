import hashlib
import random
import string

def generate_random_string(length=32):
    """Generate a random string of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def find_hash_with_double_zeros():
    """Generate hashes until one starts with two consecutive zeros."""
    for i in range(1000):
        random_string = generate_random_string()
        hash_object = hashlib.sha256(random_string.encode())
        hash_hex = hash_object.hexdigest()

        if hash_hex.startswith("00"):
            print(f"Hash found after {i + 1} attempts: {hash_hex}")
            return True

    print("No hash starting with two consecutive zeros was found in 1000 attempts.")
    return False

if __name__ == "__main__":
    find_hash_with_double_zeros()