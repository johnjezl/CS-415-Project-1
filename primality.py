import random

# Psuedocode:
#
# modexp(base, exp, mod)
#   Input: base (integer), exp (integer), mod (integer)
#   Output: integer - (base^exp) mod mod
#   Relationship:
#   Precondition: exp >= 0, mod > 0
#   result = 1
#   base = base mod mod
#   while exp > 0
#     if exp is odd:
#       result = (result * base) mod mod
#     exp = exp // 2
#     base = (base * base) mod mod
#   return result
#
# primality(N)
#   Input: N (integer)
#   Output: string ("yes" or "no") - is N prime?
#   Relationship:
#   Precondition: N > 0
#   if N == 2 
#       return "yes"
#   if N is even 
#       return "no"
#   a = random integer between 2 and N-1
#   if modexp(a, N-1, N) == 1 
#       return "yes"
#   else
#       return "no"
#
# primality2(N, k)
#   Input: N (integer), k (integer)
#   Output: string ("yes" or "no") - is N prime?
#   Relationship:
#   Precondition: N > 0, k > 0
#   if N == 2
#       return "yes"
#   if N is even
#       return "no"
#   for i from 1 to k
#     a = random integer between 2 and N-1
#     if modexp(a, N-1, N) != 1
#       return "no"
#   return "yes"
#
# primality3(N, k)
#   Input: N (integer), k (integer)
#   Output: string ("yes" or "no") - is N prime?
#   Relationship:
#   Precondition: N > 0, k > 0
#   if N <= 1 
#       return "no"
#   if N is in [2, 3, 5, 7, 11]
#        return "yes"
#   for each prime in [2, 3, 5, 7, 11]
#     if N is divisible by prime
#        return "no"
#   return primality2(N, k)


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


# Test primality 
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

