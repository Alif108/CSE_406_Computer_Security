from AES.encrypt import *

# text = input("Enter your plaintext: ")
# key = input("Enter your key: ")
text = "CanTheyDoTheirFe"
key = "BUET CSE17 Batch"

print("Plain Text: ")
print(text, end=" ")
print("[In ASCII]")
print_in_hex(input_plaintext(text).flatten(), 1)
print("[In HEX]")
print()

print("Key: ")
print(key, end=" ")
print("[In ASCII]")
print_in_hex(input_key(key).flatten(), 1)
print("[In HEX]")
print()

print("Cipher Text: ")
ciphertext = encrypt_AES(plaintext=text, keytext=key)
print_in_hex(ciphertext, 2)
print("[In HEX]")
print()