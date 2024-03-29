from AES.key import *
from AES.helper import *
from timeit import default_timer as timer


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


def encrypt_AES(plaintext, key):
    """
    :param plaintext: a string containing the text to be encrypted
    :param key: a string that will be used to encrypt
    :return: state_matrix: 2D list
             key_scheduling_time = time of key generation (in seconds)
    """
    state_matrix = plaintext_to_hex(plaintext)

    key_scheduling_time = timer()
    round_keys = key_expansion(key)
    key_scheduling_time = timer() - key_scheduling_time

    # ROUND 0
    state_matrix = add_round_key(state_matrix=state_matrix, round_keys=round_keys, round=0, decryption=ENCRYPT)

    # ROUND 1 to 9
    for round in range(1, 10):
        state_matrix = sub_bytes(state_matrix, 2)
        state_matrix = shift_row(state_matrix)
        state_matrix = mix_column(state_matrix)
        state_matrix = add_round_key(state_matrix, round_keys, round, ENCRYPT)

    # ROUND 10
    state_matrix = sub_bytes(state_matrix, 2)
    state_matrix = shift_row(state_matrix)
    state_matrix = add_round_key(state_matrix, round_keys, 10, ENCRYPT)

    return state_matrix, key_scheduling_time
