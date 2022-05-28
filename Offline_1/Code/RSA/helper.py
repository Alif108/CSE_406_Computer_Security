from BitVector import *


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


def modular(base, exponent, m):
    """
    :param base:
    :param exponent:
    :param m:
    :return: base^exponent mod m
    """
    res = 1

    base = base % m

    if base == 0:
        return 0

    while exponent > 0:
        if (exponent & 1) == 1:
            res = (res * base) % m

        exponent = exponent >> 1
        base = (base * base) % m

    return res
