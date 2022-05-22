from AES.bitvectordemo import *


ENCRYPT = 0
DECRYPT = 1


def circular_left_shift(array):
    """
    :param array: 1D array of any size
    :return: 1D left shifted array
    """
    temp = array[0]
    for i in range(1, len(array)):
        array[i-1] = array[i]
    array[len(array)-1] = temp
    return array


def circular_right_shift(array):
    """
    :param array: 1D array of any size
    :return: 1D left shifted array
    """
    temp = array[len(array)-1]
    for i in reversed(range(0, len(array)-1)):
        array[i+1] = array[i]
    array[0] = temp
    return array


def sub_bytes(array, dim):
    """
    :param array: array (1D/2D)
    :param dim: dimension of array
    :return: 1D/2D array, entries substituted with S-BOX value (string)
    """
    if dim == 1:
        for i in range(len(array)):
            # int_val = int(array[i], 0)
            int_val = array[i]
            s_box_val = Sbox[int_val]
            array[i] = s_box_val

    elif dim == 2:
        for i in range(len(array)):
            for j in range(len(array[0])):
                # int_val = int(array[i], 0)
                int_val = array[i][j]
                s_box_val = Sbox[int_val]
                array[i][j] = s_box_val

    return array


def elementwise_xor(array1, array2):
    """
    :param array1: 1D array of length l
    :param array2: 1D array of length l
    :return: 1D array of length l
    """

    if len(array1) != len(array2):
        print("Elementwise-XOR: Dimensions of the two arrays don't match")
        exit(1)

    array = []

    for i in range(len(array1)):
        array.append(array1[i] ^ array2[i])

    return array


def add_round_key(state_matrix, round_keys, round, decryption):
    """
    :param state_matrix: 2D list
    :param round_keys: 2D list
    :param round: integer
    :param decryption: boolean, 0->encryption, 1->decryption
    :return:
    """
    if round == 0 and not decryption:
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


def print_rounds_keys(round_keys):
    """
    :param round_keys: 3D array containing all the rounds' keys
    :return:
    """
    round = 0
    for i in round_keys:
        print("Round %d:" % round, end=" ")
        for j in i:
            for k in j:
                print(hex(k), end=" ")
        print()
        round += 1


def print_in_hex(array, dim):
    """
    :param array: 2D array with integer values
    :return:
    """
    if dim == 1:
        for i in range(len(array)):
            print(hex(array[i]), end=" ")
    elif dim == 2:
        for i in range(len(array)):
            for j in range(len(array[0])):
                print(hex(array[i][j]), end=" ")
            print()


def transpose(matrix1):
    """
    :param matrix1: 2D list with dim (m x n)
    :return: 2D list with dim (n x m)
    """
    matrix2 = [[row[i] for row in matrix1] for i in range(len(matrix1[0]))]
    return matrix2
