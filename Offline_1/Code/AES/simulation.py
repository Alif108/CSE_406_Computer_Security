from AES.encrypt import *
from AES.decrypt import *
import time

# text = input("Enter your plaintext: ")
# key = input("Enter your key: ")

size = 16                                       # in bytes
plaintext = "CanTheyDoTheirFest?"
key = "BUET CSE17 Batch"

padded_plaintext = pad_plaintext(plaintext, size)

for text in padded_plaintext:
    print("Plain Text: ")
    print(text, end=" ")
    print("[In ASCII]")
    print_in_hex(plaintext_to_hex(text).flatten(), 1)
    print("[In HEX]")
    print()

    print("Key: ")
    print(key, end=" ")
    print("[In ASCII]")
    print_in_hex(input_key(key).flatten(), 1)
    print("[In HEX]")
    print()

    encryption_time = time.time()
    ciphertext, key_schedule_time = encrypt_AES(plaintext=text, key=key)
    encryption_time = time.time() - encryption_time

    print("Cipher Text: ")
    print_in_hex(ciphertext, 2)
    print("[In HEX]")
    print(convert_to_ASCII_string_AES(ciphertext), end=" ")
    print("[In ASCII]")
    print()

    decryption_time = time.time()
    deciphertext = decrypt_AES(ciphertext=ciphertext, key=key)
    decryption_time = time.time() - decryption_time

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

