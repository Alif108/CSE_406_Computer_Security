import os
import pathlib

directory = "Don’t Open This"
parent_dir = pathlib.Path().resolve()
path = os.path.join(parent_dir, directory)

CONFIRMATION = "YES"

bits = 128                              # bits in prime number (RSA)
size = 16                               # chunk size of plaintext (AES)
