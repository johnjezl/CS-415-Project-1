from random_prime_generator import generate_random_prime
from primality import primality3


# Test generating random primes of varying bit lengths and k values
datasets = [[10,5],[20,10],[30,15],[40,20],[50,25],[60,30],[70,35],[80,40],[90,45],[100,50]]

for n,k in datasets:
    prime = generate_random_prime(n, k)
    print(f"Generated {n}-bit prime: {prime}")
    print(f"Binary representation: {bin(prime)}")
    print(f"Verification with primality3: {primality3(prime, k)}")
