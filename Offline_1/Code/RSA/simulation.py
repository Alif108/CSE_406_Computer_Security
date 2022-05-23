from RSA.RSA_algorithm import *


plaintext = "HAHA VODOXXX"
k = 16

keys = key_generation(k)
public_key = keys[0]
private_key = keys[1]

print("Public Key: ", end="")
print(public_key)
print("Private Key: ", end="")
print(private_key)

ciphertext = encrypt(plaintext, public_key)
print(ciphertext)

deciphertext = decrypt(ciphertext, private_key)
print(deciphertext)