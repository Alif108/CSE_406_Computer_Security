from RSA.RSA_algorithm import *


plaintext = "This is no place for no hero, This is no place for a better man to call home."
k = 64

keys = key_generation(int(k/2))
public_key = keys[0]
private_key = keys[1]

print("Public Key: ", end="")
print(public_key)
print("Private Key: ", end="")
print(private_key)

ciphertext = encrypt_RSA(plaintext, public_key)
print(ciphertext)

deciphertext = ""
deciphertext_list = decrypt_RSA(ciphertext, private_key)

for i in deciphertext_list:
    deciphertext += i

print(deciphertext)

if plaintext == deciphertext:
    print("Plaintext and Deciphertext Matched")