from AES.decrypt import *
from AES.helper import *
import socket

s = socket.socket()                                             # create a socket object

port = 12345                                                    # define the port

s.connect(('127.0.0.1', port))                                  # connect to the server on local computer

no_of_chunks = int(s.recv(1024).decode())                       # receive total number of chunks
print("Total number of chunks: %d" % no_of_chunks)

key = "BUET CSE17 Batch"                                        # TODO: encrypt key

# --------------- receiving cipher text --------------- #
for i in range(no_of_chunks):                                   # iterate over total number of chunks
    ciphertext = s.recv(1024).decode()
    ciphertext = transpose(plaintext_to_hex(ciphertext))
    deciphertext = decrypt_AES(ciphertext, key)
    print(convert_to_ASCII_string_AES(deciphertext))

# encrypted_AES_key = s.recv(1024).decode()
# print(encrypted_AES_key)

# close the connection
s.close()

