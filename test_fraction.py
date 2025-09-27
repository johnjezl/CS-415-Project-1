from fraction import Fraction

# Test basic math operations
f1 = Fraction(1, 2)  # 1/2
f2 = Fraction(1, 3)  # 1/3

print(f"1/2 + 1/3 = {f1.add(f2)}")  # Should be 5/6
print(f"1/2 - 1/3 = {f1.subtract(f2)}")  # Should be 1/6
print(f"1/2 * 1/3 = {f1.multiply(f2)}")  # Should be 1/6
print(f"1/2 / 1/3 = {f1.divide(f2)}")  # Should be 3/2

print(f"1/2 == 1/3: {f1.equals(f2)}")  # False
print(f"1/2 < 1/3: {f1.less_than(f2)}")   # False

# Test digit extraction
print(f"First digit of 1/2: {f1.get_decimal_digit(1)}")  # Should be 5
print(f"Second digit of 1/3: {f2.get_decimal_digit(2)}")  # Should be 3

# Test harmonic sum
print(f"5th digit of H3: {Fraction.hdigit(3, 5)}")