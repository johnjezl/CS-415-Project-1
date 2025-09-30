from fraction import Fraction

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
