import random
from primality import *
from random_prime_generator import generate_random_prime
from gcd import gcd 

def find_inverse(a, b):
    x, y, d = e_gcd(b, a)
    while (y < 0):
        y = y + b
    return y

def e_gcd(x, y):
    if (x < y):
        e_gcd(y, x)
    if (y == 0):
        return 1, 0, x
    x2, y2, d = e_gcd(y, x % y)
    return y2, x2 - (x//y * y2), d

# problem 4 main function
def generate_rsa_keys(bits, k):
    # generate primes and compute mods to be used
    factor1 = generate_random_prime(bits, k)
    factor2 = generate_random_prime(bits, k)
    mod = factor1 * factor2
    key_mod = (factor1 - 1) * (factor2 - 1)

    while True:
        # generate random (exactly) 10 bit integer
        e_key = random.randint(512, 1023)
        # test validity, must be relatively prime to key_mod and have an inverse other than 1
        if (gcd(e_key, key_mod) == 1):
            d_key = find_inverse(e_key, key_mod)
            if (d_key == 1):
                continue
            else:
                return factor1, factor2, mod, e_key, d_key

# problem 5 main function
def rsa(mod, e_key, d_key, message):
    encrypted = modexp(message, e_key, mod)
    decrypted = modexp(encrypted, d_key, mod)

    return encrypted, decrypted
