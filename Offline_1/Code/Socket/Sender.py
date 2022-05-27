from AES.encrypt import *
from RSA.RSA_algorithm import *
from Socket.configuration import *
import socket
import os

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

    # ----------- creating a directory -------------- #

    if not os.path.isdir(path):
        os.mkdir(path)
    print("Directory '% s' created" % directory)
    print()

    # ----------------- input plaintext and key ------------------------- #

    plaintext = input("Enter your plaintext: ")
    key = input("Enter your key: ")
    # plaintext = "CanTheyDoTheirFest?"
    # key = "BUET CSE17 Batch"

    key = pad_key(key, size)
    padded_plaintext = pad_plaintext(plaintext, size)                  # store plaintext into chunks
    client_socket.send(str(len(padded_plaintext)).encode())            # sending the total number of the chunks

    # ------------- sending cipher text (AES encrypted) ----------------- #

    for text in padded_plaintext:
        ciphertext, key_time = encrypt_AES(plaintext=text, key=key)
        ciphertext = convert_to_ASCII_string_AES(ciphertext)
        client_socket.send(ciphertext.encode())
        print("Ciphertext %s sent" % ciphertext)

        if client_socket.recv(1024).decode() != CONFIRMATION:           # receive confirmation
            print("CIPHERTEXT: Confirmation not received")
            exit(1)

    print("Ciphertext sent successfully")
    print()

    # ------------------------------------------------------------------ #

    # -------------- sending AES key (RSA encrypted) ------------------- #
    keys = key_generation(int(bits/2))
    public_key = keys[0]
    private_key = keys[1]
    encrypted_AES_key = encrypt_RSA(plaintext=key, public_key=public_key)   # encrypting the AES key

    client_socket.send(str(len(encrypted_AES_key)).encode())                # sending encrypted_key length
    if client_socket.recv(1024).decode() != CONFIRMATION:                   # receive confirmation
        print("AES ENCRYPTED LENGTH: Confirmation not received")
        exit(1)

    print("Encrypted AES key: ", end="")
    print(encrypted_AES_key)
    for i in encrypted_AES_key:
        client_socket.send(str(i).encode())                                 # send key
        if client_socket.recv(1024).decode() != CONFIRMATION:               # receive confirmation
            print("ENCRYPTED AES KEY: Confirmation not received")
            exit(1)
    print("Encrypted key sent successfully")
    print()

    # ----------------------------------------------------------------- #

    # --------------------- sending public key (PUK) ------------------- #

    print("Public Key: ", end="")
    print(public_key)
    for i in public_key:
        client_socket.send(str(i).encode())
        if client_socket.recv(1024).decode() != CONFIRMATION:                      # receive confirmation
            print("PUBLIC KEY: Confirmation not received")
            exit(1)
    print("Public Key sent successfully")
    print()

    # --------------------- store private key (PRK) -------------------- #

    file = open(path + "/PRK.txt", "w+")        # open a file
    for i in private_key:
        file.write("%s\n" % str(i))             # write the private key
    file.close()

    print("Private Key Stored Successfully")
    print("Private Key: ", end="")
    print(private_key)
    print()
    client_socket.send("PRK".encode())                                              # telling the receiver about PRK
    if client_socket.recv(1024).decode() != CONFIRMATION:                           # receive confirmation
        print("PRIVATE KEY: Confirmation not received")
        exit(1)

    # ------------------------------------------------------------------ #

    # ------------------------ match plaintext ------------------------- #

    if client_socket.recv(1024).decode() != CONFIRMATION:                           # receive confirmation
        print("PLAINTEXT: Confirmation not received")
        exit(1)
    file = open(path + "/plaintext.txt", "r")
    deciphertext = file.read()

    print("Plaintext: %s" % plaintext)
    print("Deciphertext: %s" % deciphertext)

    if plaintext == deciphertext:
        print("Plaintext and Deciphertext matched")
    else:
        print("Plaintext and Deciphertext did not match")

    # ------------------------------------------------------------------ #

    client_socket.close()                           # Close the connection with the client

    break                                           # Breaking once connection closed
