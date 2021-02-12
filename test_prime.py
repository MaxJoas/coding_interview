import pandas as pd
from prime_solution import find_first_n_primes

df = pd.read_csv('./primes1000.csv')
primes = df['prime(n)']
prime_list = primes.tolist()
prime_list[0:10]


def test_find_first_n_prims_1():
    assert find_first_n_primes(1) == set(prime_list[0:1])


def test_find_first_n_prims_10():
    assert find_first_n_primes(11) == set(prime_list[0:11])


def test_find_first_n_prims_100():
    assert find_first_n_primes(100) == set(prime_list[0:100])


def test_find_first_n_prims_143():
    assert find_first_n_primes(153) == set(prime_list[0:153])
