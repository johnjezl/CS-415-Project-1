# Class: Fraction
#   Fraction arithmetic allowing numerator and denominator of
#   arbitrary size integers.
class Fraction:

    # Class initializer
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator can't be 0")

        numerator, denominator = self._reduce(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    # Greatest common divisor (Euclidean algorithm)
    def _gcd(self, a, b):
        a = abs(a)
        b = abs(b)
        while b:
            temp = b
            b = a % b
            a = temp
        return a

    # Reduce fraction to lowest terms
    def _reduce(self, p, q):
        if (p == 0):
            return 0, 1

        g = self._gcd(p, q)

        p = p // g
        q = q // g

        # Denominator must be positive
        #   Essentially, multiply the faction by -1/-1 if q < 0
        if q < 0:
            p = -p
            q = -q

        return p, q

    # Add two fractions
    def add(self, other):
        # (n1*d2 + n2*d1) / (d1*d2)
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    # Subtract two fractions
    def subtract(self, other):
        # (n1*d2 - n2*d1) / (d1*d2)
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    # Multiply two fractions
    def multiply(self, other):
        # (n1*n2) / (d1*d2)
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    # Divide two fractions
    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")

        # (n1*d2) / (d1*n2)
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        return Fraction(numerator, denominator)

    # Test equality of two fractions
    def equals(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    # Test if this fraction is less than another fraction
    def less_than(self, other):
        # Cross multiply: p1/q1 < p2/q2 iff p1*q2 < p2*q1
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    # Get the n-th digit after the decimal point
    def get_decimal_digit(self, n):
        if self.denominator == 0:
            raise ValueError("Denominator cannot be zero")

        p = abs(self.numerator)
        q = self.denominator

        remainder = p % q

        for i in range(n):
            remainder *= 10
            digit = remainder // q
            remainder = remainder % q
        return digit

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
