from fraction import Fraction

# Pseudocode for harmonic.py
#
# hsum(n)
#   Input: n (integer)
#   Output: Fraction - the harmonic sum of the first n elements
#   Relationship:  H(n) = 1 + 1/2 + 1/3 + ... + 1/n
#   Precondition: n > 0
#   if n <= 0 
#       raise exception
#   result = Fraction(0, 1)
#   for j from 1 to n
#     term = Fraction(1, j)
#     result = result.add(term)
#   return result
#
# hdigit(n, m)
#   Input: n (integer), m (integer)
#   Output: integer - the m-th digit of the n-th harmonic number (0-9)
#   Relationship:  returns the m-th digit after the decimal point in the n-th harmonic number
#   Precondition: n > 0, m > 0
#   if n <= 0 or m <= 0
#       raise exception
#   harmonic = hsum(n)
#   return harmonic.get_decimal_digit(m)

# Calculate the harmonic sum for the first n elements
def hsum(n):
    if n <= 0:
        raise ValueError("n must be positive")

    result = Fraction(0, 1) 

    for j in range(1, n + 1):
        term = Fraction(1, j)
        result = result.add(term)

    return result

# Get the m-th digit of the n-th harmonic number
def hdigit(n, m):
    if n <= 0 or m <= 0:
        raise ValueError("n and m must be positive")

    harmonic = hsum(n)
    return harmonic.get_decimal_digit(m)
