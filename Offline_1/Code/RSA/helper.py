from BitVector import *
import random

# ITERATION = 20


# def n_bit_random(n):
#     """
#     :param n: number of buts
#     :return: a random number
#     """
#     return random.randrange(2**(n-1)+1, 2**n - 1)


# def generate_prime_number(k):
#     """
#     :param k: number of bits
#     :return: a prime number of k/2 bits
#     """
#     prime = False
#     candidate = 1
#
#     while not prime:
#         candidate = n_bit_random(k/2)
#         prime = miller_rabin_test(candidate, ITERATION)
#
#     return candidate

def generate_prime_number(k):
    """ generate prime number of k bits
    :param k: number of bits
    :return:
    """
    bv = BitVector(intVal=0)
    bv = bv.gen_random_bits(k)
    check = bv.test_for_primality()

    while check * 100 < 99:
        bv = bv.gen_random_bits(k)
        check = bv.test_for_primality()

    return int(bv)


def modular(base, exponent, M):
    """
    calculates "base^exponent % M"
    """
    ret = 1
    for i in range(exponent):
        ret = (ret * base) % M

    return ret

