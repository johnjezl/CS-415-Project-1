import random
from primality import primality3

# Generate a random n-bit prime number
def generate_random_prime(n, k):
    while True:
        # Create a random binary string of length n - 2
        binary_string = ''
        for i in range(n - 2):
            random_bit = random.choice('01')  # Randomly pick '0' or '1'
            binary_string = binary_string + random_bit  # Concatenate to the string

        # The string has to end with a one (odd)
        binary_string = binary_string + '1'

        # The string has to start with a one (n bits)
        binary_string = '1' + binary_string

        # Convert to decimal form
        result = int(binary_string, 2)

        # Test primality using primality3
        if primality3(result, k) == "yes":
            return result

