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


# def modular(base, exponent, M):
#     """
#     calculates "base^exponent % M"
#     """
#     ret = 1
#     for i in range(exponent):
#         ret = (ret * base) % M
#
#     return ret

def modular(base, exponent, m):
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


# def extendedEuclidean(num1, num2):
#     """
#     This is an extension of euclid's algorithm to find gcd of two numbers
#     It solves for x, y in the following equation
#     num1 * x + num2 * y = gcd(num1, num2)
#     Refer wikipedia's page or section 31.2 in CLRS
#     """
#     if num2 == 0:
#         return (num1, 1, 0)
#
#     d, temp_x, temp_y = extendedEuclidean(num2, num1 % num2)
#
#     x, y = temp_y, temp_x - int(num1 / num2) * temp_y
#
#     return (d, x, y)
#
#
# def multiplicativeInverse(a, b, n):
#     """
#     Generating multiplicative inverse of given numbers (a,b modulo n)
#     Refer Section 31.4 CLRS
#     """
#     d, x, y = extendedEuclidean(a, n)
#     if b % d == 0:
#         temp_x = (x * (b/d)) % n
#         result = []
#         for i in range(d):
#             result.append((temp_x + i*(n/d)) % n)
#         return result
#     return []