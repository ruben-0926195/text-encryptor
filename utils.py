import os

from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def read_key():
    if not os.path.exists("key.key"):
        return False
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        return key