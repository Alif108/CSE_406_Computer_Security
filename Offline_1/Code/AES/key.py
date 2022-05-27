from AES.helper import *

# from itertools import chain
import numpy as np
import time

def input_key(text):
    """
    :param text: a string
    :return: 2D array with the string converted to its ASCII values(integer)
    """
    key_in_hex = []

    if len(text) == 16:
        # for i in text.encode('utf-8'):
        #     key_in_hex.append(hex(i))
        for i in text:
            key_in_hex.append(ord(i))

    key_in_hex = np.reshape(key_in_hex, (-1, 4))
    return key_in_hex


def add_round_constant(array, round):
    """
    :param array: 1D array of length 4
    :param round: integer
    :return: 1D array of length 4
    """
    round_constant = RoundConstant[round-1]

    for i in range(len(array)):
        array[i] = int(array[i]) ^ round_constant[i]

    return array


def func_g(w, round):
    """
    :param w: 1D array of length 4
    :return: 1D array of length 4
    """
    w = circular_left_shift(w)
    w = sub_bytes(w, 1)
    w = add_round_constant(w, round)
    return w


def key_schedule(key, round):
    """
    :param key: 1D array
    :param round: integer
    :return: 1D array
    """

    w0 = key[0]
    w1 = key[1]
    w2 = key[2]
    w3 = key[3]
    w3_dup = w3.copy()

    new_key = []

    w4 = elementwise_xor(w0, func_g(w3_dup, round))
    w5 = elementwise_xor(w1, w4)
    w6 = elementwise_xor(w5, w2)
    w7 = elementwise_xor(w6, w3)

    new_key.append(w4)
    new_key.append(w5)
    new_key.append(w6)
    new_key.append(w7)

    return new_key


def key_expansion(key_in_text):
    """
    :param key_in_text: key in plain ASCII string
    :return: array of dim 11x16
    """
    # print("KEY SCHEDULE BEFORE: %f" % time.time())
    round_keys = []
    round0_key = input_key(key_in_text)
    round_keys.append(round0_key)
    # round_keys.append(round0_key.flatten())

    round_i_key = round0_key
    for round in range(1, 11):
        new_key = key_schedule(round_i_key, round)
        round_keys.append(new_key)
        # round_keys.append(list(chain.from_iterable(new_key)))
        round_i_key = new_key

    # print("KEY SCHEDULE AFTER: %f" % time.time())
    return round_keys
