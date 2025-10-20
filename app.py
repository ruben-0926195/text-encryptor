from utils import *

def choices():
    print("\n==============================")
    print("       TEXT ENCRYPTOR")
    print("==============================\n")
    print("1. Generate Key")
    print("2. Encrypt Key")
    print("3. Decrypt Key")
    print("4. Quit")
    print("\n------------------------------")
    return int(input("Enter your choice: "))

def main():
    while True:

        choice = choices()

        if choice == 1:
            print("Generating Key...")
            generate_key()
            input("Press enter to continue...")

        elif choice == 2:
            print("Encrypt Text")
            key = read_key()
            if not key:
                print("No key found. Generate a key first.")
                input("Press enter to continue...")
                continue
            fernet = Fernet(key)
            text = input("Enter text to encrypt: ")
            if not text:
                print("Input cannot be empty.")
                input("Press enter to continue...")
                return
            encrypted = fernet.encrypt(text.encode())
            print(f"Encrypted text:{encrypted.decode()}")
            input("Press enter to continue...")

        elif choice == 3:
            print("Decrypt Text")
            key = read_key()
            if not key:
                print("No key found. Generate a key first.")
                input("Press enter to continue...")
                continue
            fernet = Fernet(key)
            text = input("Enter text to encrypt: ")
            if not text:
                print("Input cannot be empty.")
                input("Press enter to continue...")
                return
            decrypted_text = fernet.decrypt(text.encode())
            print(f"Encrypted text:{decrypted_text.decode()}")
            input("Press enter to continue...")

        elif choice == 4:
            print("Quitting")
            break

        else:
            print("\nInvalid Choice")
            input("Press enter to continue...")

if __name__ == "__main__":
    main()