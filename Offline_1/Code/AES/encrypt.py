from AES.key import *
from AES.helper import *


def input_plaintext(text):
    """
    :param text: a string
    :return: 2D array with the string converted to its ASCII values(integer)
    """
    plaintext_in_hex = []

    if len(text) == 16:
        # for i in text.encode('utf-8'):
        #     plaintext_in_hex.append(hex(i))
        for i in text:
            plaintext_in_hex.append(ord(i))

    plaintext_in_hex = np.reshape(plaintext_in_hex, (-1, 4))
    return plaintext_in_hex


def add_round_key(state_matrix, round_keys, round):
    """
    :param state_matrix: 2D array
    :param round_keys: 2D array
    :param round: integer
    :return:
    """
    if round == 0:
        state_matrix = transpose(state_matrix)
    current_round_key = transpose(round_keys[round])

    if len(state_matrix) != len(current_round_key):
        print("Add Round Key: Dimensions don't match")
        exit(1)

    if len(state_matrix[0]) != len(current_round_key[0]):
        print("Add Round Key: Dimensions don't match")
        exit(1)

    temp = []
    new_state_matrix = []

    for i in range(len(state_matrix)):
        for j in range(len(state_matrix[0])):
            temp.append(state_matrix[i][j] ^ current_round_key[i][j])
        new_state_matrix.append(temp)
        temp = []

    return new_state_matrix


def shift_row(state_matrix):
    """
    :param state_matrix: 2D list
    :return: 2D list
    """
    for i in range(len(state_matrix)):
        for j in range(i):
            circular_left_shift(state_matrix[i])
    return state_matrix


def mix_column(state_matrix):
    """
    :param state_matrix: 2D list
    :return: 2D list
    """
    if len(state_matrix) != len(Mixer):
        print("Mix Column: 1st dimension doesn't match")
        exit(1)
    if len(state_matrix[0]) != len(Mixer[0]):
        print("Mix Column: 2nd dimension doesn't match")
        exit(1)

    AES_modulus = BitVector(bitstring='100011011')

    new_state_matrix = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]

    for i in range(len(Mixer)):
        for j in range(len(state_matrix[0])):
            for k in range(len(state_matrix)):
                bv1 = Mixer[i][k]
                bv2 = BitVector(intVal=state_matrix[k][j], size=8)
                bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
                new_state_matrix[i][j] = int(new_state_matrix[i][j]) ^ int(bv3)

    return new_state_matrix


# -------------------------------------------------------#


def encrypt_AES(plaintext, keytext):
    """
    :param plaintext: a string containing the text to be encrypted
    :param keytext: a string that will be used to encrypt
    :return: state_matrix: 2D list
    """
    state_matrix = input_plaintext(plaintext)
    round_keys = key_expansion(keytext)

    state_matrix = add_round_key(state_matrix, round_keys, 0)

    for round in range(1, 10):
        state_matrix = sub_bytes(state_matrix, 2)
        state_matrix = shift_row(state_matrix)
        state_matrix = mix_column(state_matrix)
        state_matrix = add_round_key(state_matrix, round_keys, round)

    state_matrix = sub_bytes(state_matrix, 2)
    state_matrix = shift_row(state_matrix)
    state_matrix = add_round_key(state_matrix, round_keys, 10)

    return state_matrix
