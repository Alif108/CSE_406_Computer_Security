from AES.encrypt import *
from RSA.RSA_algorithm import *
import socket

k = 16                                  # bits in prime number (RSA)
size = 16                               # chunk size of plaintext (AES)

s = socket.socket()                     # create a socket object
print("Socket successfully created")

port = 12345                            # reserve a port

s.bind(('', port))                      # bind to the port      # empty string in ip field makes the server listen to
                                                                # requests coming from other computers on the network
print("socket binded to %s" % port)

s.listen(5)                             # put the socket into listening mode
print("socket is listening")


while True:
    client_socket, address = s.accept()             # Establish connection with client.
    print('Got connection from', address)

    # plaintext = input("Enter your plaintext: ")
    # key = input("Enter your key: ")
    plaintext = "CanTheyDoTheirFest?"
    key = "BUET CSE17 Batch"

    padded_plaintext = get_uniform_chunks(plaintext, size)

    print("Total number of chunks: %d" % len(padded_plaintext))
    client_socket.send(str(len(padded_plaintext)).encode())            # sending the total number of the chunks

    # ------------- sending cipher text (AES encrypted) ----------------- #
    for text in padded_plaintext:
        ciphertext = encrypt_AES(plaintext=text, key=key)
        ciphertext = convert_to_ASCII_string_AES(ciphertext)
        client_socket.send(ciphertext.encode())
        print("Ciphertext %s sent" % ciphertext)
    print("Ciphertext sent successfully")
    # ------------------------------------------------------------------ #

    # ------------- sending AES key (RSA encrypted) ------------------- #
    # keys = key_generation(k)
    # public_key = keys[0]
    # private_key = keys[1]
    # encrypted_AES_key = encrypt_RSA(key, public_key)
    # client_socket.send(bytes(encrypted_AES_key))
    # print("Encrypted key sent successfully")

    client_socket.close()                           # Close the connection with the client

    break                                           # Breaking once connection closed
