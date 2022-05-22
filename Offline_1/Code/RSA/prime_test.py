import random
import decimal

decimal.getcontext().prec = 100


def n_bit_random(n):
    """
    :param n: number of buts
    :return: a random number
    """
    return random.randrange(2**(n-1)+1, 2**n - 1)


def miller_rabin_test(n, iterations):
    """
    :param n: candidate to be tested
    :param iterations: number of iterations
    :return: True if prime, False if composite
    """
    d = n - 1
    r = 0
    while d % 2 == 0:
        d = d/2
        r += 1

    for i in range(iterations):
        a = random.randrange(2, n - 2)
        x = (a**d) % n
        if (x != 1) and (x != n-1):
            for j in range(r-1):
                x = x*x % n
                if x == 1:
                    return False
            if x != n-1:
                return False
    return True
