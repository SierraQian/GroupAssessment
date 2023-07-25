# problem1_func.py

def find_gcd(a, b):
    # Check if a and b are positive integers
    if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0:
        raise Exception("Both inputs must be positive integers.")

    # Euclidean Algorithm to find the GCD
    while b:
        a, b = b, a % b
    return a
