from AES.key import *
from AES.helper import *
from AES.bitvectordemo import *


def inverse_shift_row(state_matrix):
    """
    :param state_matrix: 2D list
    :return: 2D list
    """
    for i in range(len(state_matrix)):
        for j in range(i):
            circular_right_shift(state_matrix[i])
    return state_matrix


def inverse_sub_bytes(array, dim):
    """
    :param array: array (1D/2D)
    :param dim: dimension of array
    :return: 1D/2D array, entries substituted with S-BOX value (string)
    """
    if dim == 1:
        for i in range(len(array)):
            int_val = array[i]
            s_box_val = InvSbox[int_val]
            array[i] = s_box_val

    elif dim == 2:
        for i in range(len(array)):
            for j in range(len(array[0])):
                int_val = array[i][j]
                s_box_val = InvSbox[int_val]
                array[i][j] = s_box_val

    return array


def inverse_mix_column(state_matrix):
    """
    :param state_matrix: 2D list
    :return: 2D list
    """
    if len(state_matrix) != len(InvMixer):
        print("Mix Column: 1st dimension doesn't match")
        exit(1)
    if len(state_matrix[0]) != len(InvMixer[0]):
        print("Mix Column: 2nd dimension doesn't match")
        exit(1)

    AES_modulus = BitVector(bitstring='100011011')

    new_state_matrix = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]

    for i in range(len(InvMixer)):
        for j in range(len(state_matrix[0])):
            for k in range(len(state_matrix)):
                bv1 = InvMixer[i][k]
                bv2 = BitVector(intVal=state_matrix[k][j], size=8)
                bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
                new_state_matrix[i][j] = int(new_state_matrix[i][j]) ^ int(bv3)

    return new_state_matrix


def decrypt_AES(ciphertext, key):
    round_keys = key_expansion(key)

    state_matrix = add_round_key(ciphertext, round_keys, 10)

    for round in reversed(range(1, 10)):
        state_matrix = inverse_shift_row(state_matrix)
        state_matrix = inverse_sub_bytes(state_matrix, 2)
        state_matrix = add_round_key(state_matrix, round_keys, round)
        state_matrix = inverse_mix_column(state_matrix)

    state_matrix = inverse_shift_row(state_matrix)
    state_matrix = inverse_sub_bytes(state_matrix, 2)
    state_matrix = add_round_key(state_matrix, round_keys, 0)

    return state_matrix
