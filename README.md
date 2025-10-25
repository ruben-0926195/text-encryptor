## Description
Python console application for encrypting and decrypting text using symmetric encryption.
The application uses Fernet part of Python's cryptography package. This package provides symmetric encryption, decryption and key generation.

## Key Management
Option 1 generates a key which is stored locally in a file named key.key.
This key is used to encrypt and decrypt the user text input. The file is excluded from the repository using gitignore.

## Installation
##### Install the required Python packages
```bash
pip install -r requirements.txt
```

##### Run the app
```bash
python app.py
```

##### Menu options
```bash
===================================
         TEXT ENCRYPTOR
===================================

[1] Generate new key
[2] Encrypt text
[3] Decrypt text
[4] Quit
-----------------------------------
```

