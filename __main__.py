from rsa import *
from fraction import Fraction
from harmonic import hdigit
from primality import *

def problem1_tester():
    print()
    print("Fractions")
    print("=================")
    print("Enter 2 fractions")

    # create fractions
    num_a = int(input("Numerator A: "))
    denom_a = int(input("Denominator A (non-zero): "))
    num_b = int(input("Numerator B: "))
    denom_b = int(input("Denominator B (non-zero): "))
    a = Fraction(num_a, denom_a)
    b = Fraction(num_b, denom_b)

    # test operators
    print(f"A + B = {a.add(b)}")
    print(f"A - B = {a.subtract(b)}")
    print(f"A * B = {a.multiply(b)}")
    print(f"A / B = {a.divide(b)}")

    print(f"A == B: {a.equals(b)}")
    print(f"A < B: {a.less_than(b)}")

    # test digit extraction
    print("Select nth decimal digit to display")
    dec_digit = int(input("Enter n: "))
    print(f"{dec_digit}th digit of A: {a.get_decimal_digit(dec_digit)}")
    print(f"{dec_digit}th digit of B: {b.get_decimal_digit(dec_digit)}")

    # test harmonic sum
    print("Select mth digit of the harmonic sum Hn to display")
    digit_m = int(input("Enter m: "))
    series_n = int(input("Enter n: "))
    print(f"{digit_m}th digit of H{series_n}: {hdigit(series_n, digit_m)}")

    return menu()

def problem2_tester():
    print()
    print("Primality testing")
    print("=================")
    number = int(input("Enter a number to be tested: "))
    precision = int(input("Enter primality test precision: "))
    if primality3(number, precision) == "yes":
        print("Yes, this number is (likely) prime")
    else:
        print("No, this number is not prime")

    return menu()

def problem5_tester():
    print()
    print("RSA")
    print("=================")

    # get user inputs
    bits = int(input("Enter the number of bits to be used for the prime key's factors: "))
    precision = int(input("Enter primality test precision: "))
    message = int(input("Enter the message (numeric) to be encrypted: "))

    # call rsa
    factor1, factor2, mod, encryption_key, decryption_key = generate_rsa_keys(bits, precision)
    encrypted, decrypted = rsa(mod, encryption_key, decryption_key, message)

    # output results
    print ("p = ", factor1, ", q = ", factor2, ", N = ", mod, ", E = ", encryption_key, ", D = ", decryption_key)
    print("Encrypted message: ", encrypted)
    print("Decrypted message: ", decrypted)
    if (message == decrypted):
        print("Yes, the message was correctly decrypted")
    else:
        print("No, the message was not correctly decrypted")

    return menu()

def menu():
    # print menu
    print()
    print("Menu")
    print("=================")
    print("1. Fractions")
    print("2. Primality test")
    print("3. RSA")
    print("4. Exit")
    print("Enter 1, 2, 3, or 4: ")

    # get input and validate
    usr_input = int(input())
    while usr_input not in [1, 2, 3, 4]:
        usr_input = int(input("Invalid input, enter 1, 2, 3, or 4: "))

    # switch to relevant problem
    if usr_input == 1:
        problem1_tester()
    elif usr_input == 2:
        problem2_tester()
    elif usr_input == 3:
        problem5_tester()

    return

menu()