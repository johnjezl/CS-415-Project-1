import random
from primality import primality3

# Pseudocode for random_prime_generator.py
#
# generate_random_prime(n, k)
#   Input: n (integer, number of bits), k (integer, # of test iterations)
#   Output: integer (n-bit prime number)
#   Pre-Confdtion: n >= 2, k > 0
#   Relationship:
#   while True
#     binary_string = empty string
#     for i from 0 to n-3
#       random_bit = randomly choose '0' or '1'
#       binary_string = binary_string + random_bit
#     binary_string = append 1 to make odd
#     binary_string = prepend 1 to make n bits
#     result = convert binary_string to decimal
#     if primality3(result, k) == "yes"
#       return result

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

