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
    