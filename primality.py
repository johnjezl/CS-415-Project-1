import random


# Compute modular exponentiation
def modexp(base, exp, mod):
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    
    return result


# Test primality (Fermat's Little Theorem)
def primality(N):
    if N == 2:
        return "yes"
    if N % 2 == 0:
        return "no"
    
    # Choose random value
    a = random.randint(2, N - 1)
    
    # Test 
    if modexp(a, N - 1, N) == 1:
        return "yes"
    else:
        return "no"

# Test primality with k iterations
def primality2(N, k):
    if N == 2:
        return "yes"
    if N % 2 == 0:
        return "no"
    
    for _ in range(k):
        # Choose random value
        a = random.randint(2, N - 1)
        
        # Test
        if modexp(a, N - 1, N) != 1:
            return "no"
    
    return "yes"

# Test primality with initial checks for "known" primes
def primality3(N, k):
    if N <= 1:
        return "no"
    
    # Check if N is a "known" prime numbers
    known_primes = [2, 3, 5, 7, 11]
    if N in known_primes:
        return "yes"
    
    # Test divisibility by "known"" primes
    for prime in known_primes:
        if N % prime == 0:
            return "no"
    
    # Do the rest of the testing...
    return primality2(N, k)

