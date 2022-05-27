from RSA.helper import *
import math
from BitVector import *


def key_generation(k):
    """
    :param k: size (in bit) of keys
    :return: keys -> 2D array -> [public key, private key]
    """
    p = generate_prime_number(k)
    q = generate_prime_number(k)

    while p == q:
        q = generate_prime_number(k)

    n = p * q
    phi = (p-1) * (q-1)

    # calculating e
    while True:
        e = random.randrange(2, phi)
        if math.gcd(e, phi) == 1:
            break

    # calculating d
    d = 1
    bv_modulus = BitVector(intVal=phi)
    bv = BitVector(intVal=e)
    bv_result = bv.multiplicative_inverse(bv_modulus)
    if bv_result is not None:
        d = int(bv_result)

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
    :return: encrypted ASCII value -> integer
    """
    P = ord(P)                  # taking the ASCII value
    e = public_key[0]
    n = public_key[1]

    return modular(P, e, n)     # C = P^e mod n


def decrypt_char(C, private_key):
    """
    :param C: Ciphertext character to be decrypted
    :param private_key:
    :return: decrypted character (char)
    """
    d = private_key[0]
    n = private_key[1]

    return chr(int(modular(C, d, n)))       # P = C^d mod n


def encrypt_RSA(plaintext, public_key):
    """
    :param plaintext: plaintext to be encrypted [string]
    :param public_key: 1D array -> [e, n]
    :return: ciphertext (1D array of integers)
    """
    ciphertext = []

    for i in plaintext:
        ciphertext.append(encrypt_char(i, public_key))

    return ciphertext


def decrypt_RSA(ciphertext, private_key):
    """
    :param ciphertext: Ciphertext that is to be decrypted -> 1D array of ASCII values (integers)
    :param private_key: 1D array -> [d, n]
    :return: deciphertext -> 1D array of characters
    """
    deciphertext = []

    for i in ciphertext:
        deciphertext.append(decrypt_char(i, private_key))

    return deciphertext
