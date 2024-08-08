#!/usr/bin/python3
"""
Module to calculate the minimum number of operations needed to
achieve exactly n 'H' characters using only Copy All and Paste operations.

Function:
    minOperations(n): Computes the minimum number of operations needed
    to get exactly n 'H' characters.
    
    Parameters:
        n (int): The target number of 'H' characters to be achieved.
    
    Returns:
        int: The minimum number of operations required. Returns 0 if
        n is less than or equal to 1.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations required to get exactly
    n 'H' characters using Copy All and Paste operations.
    
    Args:
        n (int): The number of 'H' characters to achieve.
        
    Returns:
        int: The minimum number of operations needed. Returns 0 if n
        is less than or equal to 1.
    """
    if n <= 1:
        return 0  # No operations needed for 1 or less characters

    total_operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            total_operations += factor
            n //= factor
        factor += 1

    return total_operations
