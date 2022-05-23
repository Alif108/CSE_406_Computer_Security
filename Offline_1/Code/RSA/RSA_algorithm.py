import math
from RSA.prime_test import *


def key_generation(k):
    p = generate_prime_number(k)
    q = generate_prime_number(k)

    while p == q:
        q = generate_prime_number(k)

    print("p: %d" % p)
    print("q: %d" % q)

    n = p * q
    phi = (p-1) * (q-1)

    print("phi: %d" % phi)

    e = p
    # e = 1
    # for i in range(2, phi):
    #     if math.gcd(i, phi) == 1:       # TODO: research 'Euler's Totient'
    #         e = i
    #         break

    print("e: %d" % e)

    i = 1
    while True:
        if ((1 + i * phi) % e) == 0:
            d = (1 + i * phi) / e
            break
        i += 1

    print("d: %d" % d)
    print("i: %d" % i)

    keys = []
    public_key = [e, n]
    private_key = [int(d), n]

    keys.append(public_key)
    keys.append(private_key)

    return keys


def encrypt_char(P, public_key):
    """
    :param P: character to be encrypted
    :param public_key: 1D array -> [e, n]
    :return:
    """
    P = ord(P)                  # taking the ASCII value
    e = public_key[0]
    n = public_key[1]
    return (P ** e) % n         # C = P^e mod n


def decrypt_char(C, private_key):
    """
    :param C: Ciphertext character to be decrypted
    :param private_key:
    :return:
    """
    d = private_key[0]
    n = private_key[1]

    return chr(int((C ** d) % n))     # P = C^d mod n


def encrypt(plaintext, public_key):
    ciphertext = []

    for i in plaintext:
        ciphertext.append(encrypt_char(i, public_key))

    return ciphertext


def decrypt(ciphertext, private_key):
    deciphertext = []

    for i in ciphertext:
        deciphertext.append(decrypt_char(i, private_key))

    return deciphertext
