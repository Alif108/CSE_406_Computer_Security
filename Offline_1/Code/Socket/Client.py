from AES.decrypt import *
from RSA.RSA_algorithm import *
from Socket.configuration import *
import socket

s = socket.socket()                                             # create a socket object

port = 12345                                                    # define the port

s.connect(('127.0.0.1', port))                                  # connect to the server on local computer

no_of_chunks = int(s.recv(1024).decode())                       # receive total number of chunks
print("Total number of chunks: %d" % no_of_chunks)

# --------------- receiving cipher text --------------- #

AES_ciphertext = []
for i in range(no_of_chunks):                                   # iterate over total number of chunks
    ciphertext = s.recv(1024).decode()
    AES_ciphertext.append(ciphertext)
    print("ciphertext %s received" % ciphertext)
    s.send(CONFIRMATION.encode())
print()
# ------------------------------------------------------- #


# ---------------- receiving encrypted key -------------- #

encrypted_AES_key = []
encrypted_key_length = int(s.recv(1024).decode())               # receiving encrypted key length
s.send(CONFIRMATION.encode())
print("encrypted key length: %d" % encrypted_key_length)

for i in range(encrypted_key_length):
    encrypted_AES_key.append(s.recv(1024).decode())
    s.send(CONFIRMATION.encode())

for i in range(len(encrypted_AES_key)):
    encrypted_AES_key[i] = int(encrypted_AES_key[i])

print("Encrypted AES key:", end=" ")
print(encrypted_AES_key)
print()

# ------------------------------------------------------- #

# ---------- receiving public key (PUK) ----------------- #

public_key = []
for i in range(2):
    public_key.append(s.recv(1024).decode())
    s.send(CONFIRMATION.encode())
    public_key[i] = int(public_key[i])

print("public key received successfully")
print("Public Key: ", end="")
print(public_key)
print()
# ------------------------------------------------------- #

# ------------- receiving private key (PRK) ------------- #
private_key = []
if s.recv(1024).decode() != "PRK":
    print("PRK not received")
    exit(1)
s.send(CONFIRMATION.encode())

file = open(path + "\PRK.txt", "r")
file_read = file.read().split("\n")
private_key.append(int(file_read[0]))
private_key.append(int(file_read[1]))
print("Private key received successfully")
print("Private Key: ", end="")
print(private_key)
# -------------------------------------------------------- #


# ------------------ decrypt AES key --------------------- #
decrypted_AES_key = decrypt_RSA(ciphertext=encrypted_AES_key, private_key=private_key)
AES_key = ""
for i in decrypted_AES_key:
    AES_key += i
print("Decrypted AES key: %s" % AES_key)
print()
# -------------------------------------------------------- #

# ---------------- decrypt cipher text ------------------- #
deciphertext = []

for text in AES_ciphertext:
    text = transpose(plaintext_to_hex(text))
    deciphertext.append(convert_to_ASCII_string_AES(decrypt_AES(text, AES_key)))
print("Deciphertext: ", end="")
print(deciphertext)
print()
# -------------------------------------------------------- #


# ----------------- write to folder ---------------------- #

file = open(path + "/plaintext.txt", "+w")
for text in deciphertext:
    file.write(text.replace("*", ""))
file.close()

s.send(CONFIRMATION.encode())

# -------------------------------------------------------- #

# close the connection
s.close()

