# gcd (euclid's algorithm)
# inputs:
#   a, b
# pre-conditions:
#   a and b are non-negative integers
# output:
#   d
# relationships:
#   d is the greatest common factor of a and b
#   i.e. the largest d such that a / d and b / d are integers
# pseudocode:
#   if a < b
#       swap a and b
#   if b = 0 (base case)
#       return a
#   else
#       return gcd(b, a mod b)

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

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
    