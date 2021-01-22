import sys
import timeit
import numpy as np

# You do not need to use these functios. The primary function needs to be
# called find_first_n_primes


def is_prime(i, primes):
    """Takes a number and a list of prime numbers and checks if the number
    is prime.

    Args:
        i - (int) number to check if it is prime.
        primes - (set) set of already found prime numbers

    Returns:
        is_prime - (bool) boolean that indicates if a number is prime

    """
    for prime in primes:
        if(i % prime == 0):
            return False
    return True


def find_first_n_primes(n):
    """Finds the first n prime numbers

    Args:
        n - (int) number that indicates how many prime numbers should be found

    Returns:
        primes - (set) set of first n prime numbers

    """
    primes = [1]
    toCheck = 2
    while(len(primes <= n):
        if(is_prime(toCheck, primes)):
            primes.append(toCheck)
        toCheck += 1
    return primes



if __name__ == '__main__':
    n = int(sys.argv[1])
    start = timeit.timeit()
    primes = find_first_n_primes(n)
    end = timeit.timeit()
    print('Execution took')
    print(start - end)
