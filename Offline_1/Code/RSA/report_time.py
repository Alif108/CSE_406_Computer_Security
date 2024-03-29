from RSA.RSA_algorithm import *
from timeit import default_timer as timer


plaintext = input("Enter your plaintext: ")
print("Plaintext: %s" % plaintext)

k_values = [16, 32, 64, 128]
report = []

for k in k_values:
    temp = []

    key_gen_time = timer()
    keys = key_generation(int(k/2))
    key_gen_time = timer() - key_gen_time

    public_key = keys[0]
    private_key = keys[1]

    # ------------- ENCRYPTION ------------- #
    encryption_time = timer()
    ciphertext = encrypt_RSA(plaintext, public_key)
    encryption_time = timer() - encryption_time

    # ------------- DECRYPTION ------------- #

    decryption_time = timer()
    deciphertext_list = decrypt_RSA(ciphertext, private_key)
    decryption_time = timer() - decryption_time

    deciphertext = ""
    for i in deciphertext_list:
        deciphertext += i

    print("k = %d" % k, end="\t")
    print("Deciphertext: %s" % deciphertext, end="\t")
    print("Keys: ", end="")
    print(keys)

    temp.append(key_gen_time)
    temp.append(encryption_time)
    temp.append(decryption_time)

    report.append(temp)

# ------------ printing the report ------------- #
print("K", end="\t\t\t\t\t")
print("Key-Generation", end="\t\t\t\t\t")
print("Encryption", end="\t\t\t\t\t")
print("Decryption", end="\t\t\t\t\t")
print()
for i in range(len(k_values)):
    print(k_values[i], end="\t\t\t\t\t")
    for j in range(len(report[i])):
        print(report[i][j], end="\t\t\t\t\t")
    print()
