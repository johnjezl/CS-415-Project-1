from primality import primality3

while(True):
    N = int(input("Enter an integer to test: "))
    k = int(input("Enter value for k: "))
        
    result = primality3(N, k)
        
    if result == "yes":
        print(f"{N} is probably prime (error probability <= 2^(-{k}))")
    else:
        print(f"{N} is not prime")
