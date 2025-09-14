#!/usr/bin/python3
"""
This module contains a method to calculate the fewest number of operations
to achieve exactly 'n' H characters in a text file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The min number of operations, or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
            divisor = 2  # Reset divisor to find prime factors
        else:
            divisor += 1
    return operations
