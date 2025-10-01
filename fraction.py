from gcd import gcd

# Psuedocode for Fraction class methods:
#
# __init__(numerator, denominator)
#   Input: numerator (integer), denominator (integer, default 1)
#   Output: None
#   Pre-Condition: denominator != 0
#   Relationship: Creates fraction numerator/denominator (reduced)
#   if denominator == 0 
#       raise error
#   reduce fraction
#   Set object's numerator and denominator
#
# _reduce(p, q)
#   Input: p (integer), q (integer)
#   Output: two integers (reduced_p, reduced_q) that represent the reduced form of p/q
#   Pre-Condition: q != 0
#   Relationship:
#   if p == 0
#       return (0, 1)
#   find gcd of p and q
#   divide both p and q by gcd
#   if q < 0
#       make both p and q negative to keep denominator positive
#   return (p, q)
#
# add(rhs)
#   Input: rhs (Fraction)
#   Output: Fraction that is the sum of self and rhs
#   Pre-Condition: 
#   Relationship:
#   numerator = self.numerator * rhs.denominator + rhs.numerator * self.denominator
#   denominator = self.denominator * rhs.denominator
#   return new Fraction(numerator, denominator)
#
# subtract(rhs)
#   Input: rhs (Fraction)
#   Output: Fraction that is the difference of self and rhs
#   Pre-Condition: 
#   Relationship: 
#   numerator = self.numerator * rhs.denominator - rhs.numerator * self.denominator
#   denominator = self.denominator * rhs.denominator
#   return new Fraction(numerator, denominator)
#
# multiply(rhs)
#   Input: rhs (Fraction)
#   Output: Fraction that is the product of self and rhs
#   Pre-Condition: 
#   Relationship: 
#   numerator = self.numerator * rhs.numerator
#   denominator = self.denominator * rhs.denominator
#   return new Fraction(numerator, denominator)
#
# divide(rhs)
#   Input: rhs (Fraction)
#   Output: Fraction is the quotient of self and rhs
#   Pre-Condition: rhs.numerator != 0
#   Relationship: 
#   if rhs.numerator == 0 
#       raise error
#   numerator = self.numerator * rhs.denominator
#   denominator = self.denominator * rhs.numerator
#   return new Fraction(numerator, denominator)
#
# equals(rhs)
#   Input: rhs (Fraction)
#   Output: boolean - true if self == rhs, false otherwise
#   Pre-Condition: rhs is a Fraction, both fractions are in reduced form
#   Relationship: 
#   return self.numerator == rhs.numerator and self.denominator == rhs.denominator
#
# less_than(rhs)
#   Input: rhs (Fraction)
#   Output: boolean - true if self < rhs, false otherwise
#   Pre-Condition:
#   Relationship: 
#   return self.numerator * rhs.denominator < rhs.numerator * self.denominator
#
# get_decimal_digit(n)
#   Input: n (position after decimal point)
#   Output: integer (single digit 0-9)
#   Pre-Condition: n > 0, self.denominator != 0
#   Relationship:
#   if denominator == 0
#       raise error
#   p = absolute value of numerator
#   q = denominator
#   remainder = p mod q
#   for i from 0 to n-1
#     remainder = remainder * 10
#     digit = remainder // q
#     remainder = remainder mod q
#   return digit

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

    # Reduce fraction to lowest terms
    def _reduce(self, p, q):
        if (p == 0):
            return 0, 1

        g = gcd(p, q)

        p = p // g
        q = q // g

        # Denominator must be positive
        #   Essentially, multiply the faction by -1/-1 if q < 0
        if q < 0:
            p = -p
            q = -q

        return p, q

    # Add two fractions
    def add(self, rhs):
        # (n1*d2 + n2*d1) / (d1*d2)
        numerator = self.numerator * rhs.denominator + rhs.numerator * self.denominator
        denominator = self.denominator * rhs.denominator

        return Fraction(numerator, denominator)

    # Subtract two fractions
    def subtract(self, rhs):
        # (n1*d2 - n2*d1) / (d1*d2)
        numerator = self.numerator * rhs.denominator - rhs.numerator * self.denominator
        denominator = self.denominator * rhs.denominator

        return Fraction(numerator, denominator)

    # Multiply two fractions
    def multiply(self, rhs):
        # (n1*n2) / (d1*d2)
        numerator = self.numerator * rhs.numerator
        denominator = self.denominator * rhs.denominator

        return Fraction(numerator, denominator)

    # Divide two fractions
    def divide(self, rhs):
        if rhs.numerator == 0:
            raise ValueError("Cannot divide by zero")

        # (n1*d2) / (d1*n2)
        numerator = self.numerator * rhs.denominator
        denominator = self.denominator * rhs.numerator

        return Fraction(numerator, denominator)

    # Test equality of two fractions
    def equals(self, rhs):
        return self.numerator == rhs.numerator and self.denominator == rhs.denominator

    # Test if this fraction is less than anrhs fraction
    def less_than(self, rhs):
        # Cross multiply: p1/q1 < p2/q2 iff p1*q2 < p2*q1
        return (self.numerator * rhs.denominator) < (rhs.numerator * self.denominator)

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
