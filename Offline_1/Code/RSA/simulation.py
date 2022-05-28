from RSA.RSA_algorithm import *

bits = 128                  # number of bits in keys
plaintext = input("Enter you plaintext: ")

keys = key_generation(int(bits/2))
public_key = keys[0]
private_key = keys[1]

print("Public Key: ", end="")
print(public_key)
print("Private Key: ", end="")
print(private_key)

ciphertext = encrypt_RSA(plaintext, public_key)
print("Ciphertext: ", end="")
print(ciphertext)

deciphertext = ""
deciphertext_list = decrypt_RSA(ciphertext, private_key)

for i in deciphertext_list:
    deciphertext += i

print("Deciphertext: %s" % deciphertext)

if plaintext == deciphertext:
    print("Plaintext and Deciphertext Matched")
else:
    print("Plaintext and Deciphertext Did not Match :( ")