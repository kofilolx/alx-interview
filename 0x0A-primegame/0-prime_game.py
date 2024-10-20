#!/usr/bin/python3
"""Prime game module"""


def generate_primes(limit):
    """Generate a list of prime numbers up to
        'limit' using the Sieve of Eratosthenes algorithm.
    """
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return [num for num in range(2, limit + 1) if is_prime[num]]


def isWinner(x, nums):
    """Determines the winner after multiple rounds of the prime game."""
    scores = {'Maria': 0, 'Ben': 0}

    # Generate prime numbers up to the maximum number in nums
    prime_numbers = generate_primes(max(nums))

    for n in nums[:x]:
        if n == 1 or n in prime_numbers:
            # Ben wins if n is 1 or a prime number
            scores['Ben'] += 1
        else:
            # Maria wins if n is not a prime number
            scores['Maria'] += 1

    if scores['Maria'] > scores['Ben']:
        return 'Maria'
    elif scores['Ben'] > scores['Maria']:
        return 'Ben'
    return None
