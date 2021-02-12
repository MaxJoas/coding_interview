import sys
import timeit
import numpy as np


def is_prime(i, primes):
    """Takes a number and a list of prime numbers and checks if the number
    is prime.

    Args:
        i - (int) number to check if it is prime.
        primes - (list) set of already found prime numbers

    Returns:
        is_prime - (bool) boolean that indicates if a number is prime

    """
    is_prime = False
    for prime in list(primes):
        if np.sqrt(i) < prime:
            return not is_prime
        if not (i == prime or i % prime):
            return is_prime
    return not is_prime


def find_first_n_primes(n):
    """Finds the first n prime numbers

    Args:
        n - (int) number that indicates how many prime numbers should be found

    Returns:
        primes - (set) set of first n prime numbers

    """
    primes = []
    to_check = 2

    while len(primes) < n:
        if is_prime(to_check, primes):
            primes.append(to_check)
        to_check += 1
    print('The first {} prime numbers are: {}'.format(n, primes))
    return set(primes)


find_first_n_primes(10)

if __name__ == '__main__':
    print('maine')
    n = int(sys.argv[1])
    start = timeit.timeit()
    primes = find_first_n_primes(n)
    end = timeit.timeit()
    print('Execution took')
    print(start - end)
