from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt(text, key):
    pass

def decrypt(text, key):
    pass
