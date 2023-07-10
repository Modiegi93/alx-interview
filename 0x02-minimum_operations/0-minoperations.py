#!/usr/bin/python3
"""
Method that calculates the fewest number of operations needed
"""


def minOperations(n):
    """Returns an integer"""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1
    
    return operations
