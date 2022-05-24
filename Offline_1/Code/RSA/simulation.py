from RSA.RSA_algorithm import *


plaintext = "HAHA VODOXXX"
k = 16

keys = key_generation(int(k/2))
public_key = keys[0]
private_key = keys[1]

print("Public Key: ", end="")
print(public_key)
print("Private Key: ", end="")
print(private_key)

ciphertext = encrypt_RSA(plaintext, public_key)
print(ciphertext)

deciphertext = decrypt_RSA(ciphertext, private_key)
print(deciphertext)