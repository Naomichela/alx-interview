#!/usr/bin/python3
"""
Calculates the minimum number of operations needed to get exactly
n H characters in the file, using only "Copy All" and "Paste".
"""

def minOperations(n):
    # If n is less than or equal to 1, it's impossible to achieve more than one character
    if n < 2:
        return 0
    
    # Initialize the number of operations
    operations = 0
    # Start with the smallest prime factor
    factor = 2
    
    # Decompose n by its prime factors
    while n > 1:
        # While n is divisible by the factor, reduce it and count the operations
        while n % factor == 0:
            operations += factor
            n /= factor
        # Move to the next factor
        factor += 1
    
    return operations

