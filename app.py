from utils import *

def choices():
    print("\n==============================")
    print("       TEXT ENCRYPTOR")
    print("==============================\n")
    print("1. Encrypt key")
    print("2. Decrypt key")
    print("3. Quit")
    print("\n------------------------------")
    return int(input("Enter your choice: "))

def main():
    while True:
        choice = choices()
        if choice == 1:
            print("Generate Key")
            input("Press enter to continue...")
        elif choice == 2:
            print("Encrypt Key")
            input("Press enter to continue...")
        elif choice == 2:
            print("Decrypt Key")
            input("Press enter to continue...")
        elif choice == 3:
            print("Quitting")
            break
        else:
            print("\nInvalid Choice")
            input("Press enter to continue...")

if __name__ == "__main__":
    main()