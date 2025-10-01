import random
from random_prime_generator import generate_random_prime
from primality import modexp
from gcd import gcd

# modular inverse calculation
# inputs:
#   a, b
# pre-conditions:
#   a and b are positive integers
#   a and b are relatively prime (gcd(a,b) = 1)
#   base
# output:
#   y
# relationship:
#   a * y = 1 (mod b), 1 <= y < b
# pseudocode:
#   call extended gcd to find x, y s.t. b * x + a * y = gcd(a, b)
#   if y is negative, add b until it's positive
#   return y

def find_inverse(a, b):
    x, y, d = e_gcd(b, a)
    while y < 0:
        y = y + b
    return y

# extended gcd
# inputs:
#   x, y
# pre-conditions:
#   x and y are positive integers
#   x > y
# outputs:
#   a, b, d
# relationship:
#    (a * x) + (b * y) = d, and gcd(x, y) = d
# pseudocode:
#   if y == 0 (base case)
#       return 1, 0, x
#   x2, y2, d = e_gcd(y, x mod y)
#   return y2, x2 - (floor(x/y) * y2), d

def e_gcd(x, y):
    if y == 0:
        return 1, 0, x
    x2, y2, d = e_gcd(y, x % y)
    return y2, x2 - (x//y * y2), d

# problem 4 main function
# inputs:
#   n_bits (number of bits prime factors should be)
#   precision (precision used by prime generator)
# pre-conditions:
#   bits and precision are positive integers
# outputs:
#   factor1, factor2, mod_key, e_key, d_key
# relationships:
#   mod_key = factor1 * factor2
#   factor1 and factor2 have n_bits bits
#   e_key, d_key such that (a^e_key)^d_key = a (mod mod_key)
# pseudocode:
#   get 2 prime factors, f1, f2
#   modulus = f1*f2
#   exp_mod = (f1 - 1) * (f2 - 1)
#   loop:
#       generate random 10 bit integer, e
#       if gcd(e, exp_mod) = 1
#           d = modular inverse of e wrt. exp_mod
#           if d != 1
#               break out of loop
#   return f1, f2, modulus, e, d

def generate_rsa_keys(n_bits, precision):
    # generate primes and compute mods to be used
    factor1 = generate_random_prime(n_bits, precision)
    factor2 = generate_random_prime(n_bits, precision)
    mod_key = factor1 * factor2
    exp_mod = (factor1 - 1) * (factor2 - 1)

    while True:
        # generate random (exactly) 10 bit integer
        e_key = random.randint(512, 1023)
        # test validity
        # must be relatively prime to exp_mod and have an inverse other than 1
        if gcd(e_key, exp_mod) == 1:
            d_key = find_inverse(e_key, exp_mod)
            if d_key == 1:
                continue
            else:
                return factor1, factor2, mod_key, e_key, d_key

# problem 5 main function
# inputs:
#   mod_key (modulus key)
#   e_key, d_key (encryption and decryption exponents)
#   message
# pre-conditions:
#   mod_key is the product of 2 prime numbers
#   e_key and d_key are exponent inverses
#   (meaning (a^e_key)^d_key = a)
#   message is non-negative and less than mod_key
# outputs:
#   encrypted message and decrypted message
# pseudocode/relationships:
#   encrypted = m^e_key mod mod_key
#   decrypted = encrypted^d_key mod mod_key

def rsa(mod_key, e_key, d_key, message):
    encrypted = modexp(message, e_key, mod_key)
    decrypted = modexp(encrypted, d_key, mod_key)

    return encrypted, decrypted