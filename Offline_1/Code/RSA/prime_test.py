import random


ITERATION = 20


def n_bit_random(n):
    """
    :param n: number of buts
    :return: a random number
    """
    return random.randrange(2**(n-1)+1, 2**n - 1)


def set_bit_number(n):
    if n == 0:
        return 0

    msb = 0
    n = int(n / 2)

    while n > 0:
        n = int(n / 2)
        msb += 1

    return 1 << msb


def witness(a, n):
    u = n - 1
    t = 0

    while u % 2 == 0:
        u = u >> 1
        t += 1

    x = 1
    mask = set_bit_number(u)

    while mask:
        x = (x * x) % n
        if u & mask:
            x = (x * a) % n
        mask = mask >> 1

    for i in range(t):
        w = x
        x = (w * w) % n
        if (x == 1) and (w != 1) and (w != n-1):
            return True

    return x != 1


def miller_rabin_test(n, trials):
    for i in range(trials):
        a = random.randrange(1, n-1)
        if witness(a, n):
            return False
    return True


def generate_prime_number(k):
    prime = False
    candidate = 1

    while not prime:
        candidate = n_bit_random(k/2)
        prime = miller_rabin_test(candidate, ITERATION)

    return candidate
