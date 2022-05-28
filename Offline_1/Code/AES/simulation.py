from AES.encrypt import *
from AES.decrypt import *
from timeit import default_timer as timer

plaintext = input("Enter your plaintext: ")
key = input("Enter your key: ")
print()

size = 16                                       # in bytes

padded_plaintext = pad_plaintext(plaintext, size)
key = pad_key(key, size)
iteration = 0

for text in padded_plaintext:
    print("Iteration: %d" % iteration)
    print()
    print("Plain Text: ")
    print(text, end=" ")
    print("[In ASCII]")
    print_in_hex(plaintext_to_hex(text).flatten(), 1)
    print("[In HEX]")
    print()

    print("Key: ")
    print(key, end=" ")
    print("[In ASCII]")
    print_in_hex(key_to_hex(key).flatten(), 1)
    print("[In HEX]")
    print()

    encryption_time = timer()
    ciphertext, key_schedule_time = encrypt_AES(plaintext=text, key=key)
    encryption_time = timer() - encryption_time

    print("Cipher Text: ")
    print_in_hex(array=ciphertext, dim=2)
    print("[In HEX]")
    print(convert_to_ASCII_string_AES(ciphertext), end=" ")
    print("[In ASCII]")
    print()

    decryption_time = timer()
    deciphertext = decrypt_AES(ciphertext=ciphertext, key=key)
    decryption_time = timer() - decryption_time

    print("Deciphered Text: ")
    print_in_hex(deciphertext, 2)
    print("[In HEX]")
    print(convert_to_ASCII_string_AES(deciphertext), end=" ")
    print("[IN ASCII]")
    print()

    print("Execution Time")
    print("Key Scheduling: %f seconds" % key_schedule_time)
    print("Encryption time: %f seconds" % encryption_time)
    print("Decryption time: %f seconds" % decryption_time)
    print()
    print()

    iteration += 1


