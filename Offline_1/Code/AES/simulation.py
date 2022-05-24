from AES.encrypt import *
from AES.decrypt import *

# text = input("Enter your plaintext: ")
# key = input("Enter your key: ")

size = 16                                       # in bytes
plaintext = "CanTheyDoTheirFest?"
key = "BUET CSE17 Batch"

padded_plaintext = get_uniform_chunks(plaintext, size)

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

    print("Cipher Text: ")
    ciphertext = encrypt_AES(plaintext=text, key=key)
    print_in_hex(ciphertext, 2)
    print("[In HEX]")
    print(convert_to_ASCII_string_AES(ciphertext), end=" ")
    print("[In ASCII]")
    print()

    print("Deciphered Text: ")
    deciphertext = decrypt_AES(ciphertext=ciphertext, key=key)
    print_in_hex(deciphertext, 2)
    print("[In HEX]")
    print(convert_to_ASCII_string_AES(deciphertext), end=" ")
    print("[IN ASCII]")
    print()
    print()

