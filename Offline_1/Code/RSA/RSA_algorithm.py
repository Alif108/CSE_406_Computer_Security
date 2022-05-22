import math


def key_generation():
    p = 13                              # TODO: generate prime numbers
    q = 11

    n = p * q
    phi = (p-1) * (q-1)

    # e = 13
    e = 1
    for i in reversed(range(phi)):
        if math.gcd(i, phi) == 1:       # TODO: research 'Euler's Totient'
            e = i
            break

    i = 1
    while True:
        if ((1 + i * phi) % e) == 0:
            d = (1 + i * phi) / e
            break
        i += 1

    keys = []
    public_key = [e, n]
    private_key = [d, n]

    keys.append(public_key)
    keys.append(private_key)

    return keys


def encrypt(P, public_key):
    """
    :param P: character to be encrypted
    :param public_key: 1D array -> [e, n]
    :return:
    """
    e = public_key[0]
    n = public_key[1]
    return (P ** e) % n      # C = P^e mod n


def decrypt(C, private_key):
    """
    :param C: Ciphertext character to be decrypted
    :param private_key:
    :return:
    """
    d = private_key[0]
    n = private_key[1]

    return (C ** d) % n     # P = C^d mod n
