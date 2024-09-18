# venv/bin/python3
'''caesar chipher'''

import sys


def encrypt(text: str) -> str:
    '''encodes plaintext'''
    encrypted: str = ""
    for char in text:
        if char.isupper():
            tmp: str = chr((ord(char) + ord("A") + 3) % 26 + ord("A"))
            encrypted += tmp
        else:
            tmp: str = chr((ord(char) + ord("A") - 3) % 26 + ord("a"))
            encrypted += tmp
    return encrypted


def decrypt(text: str) -> str:
    '''decodes cipher'''
    decrypted: str = ""
    for char in text:
        if char.isupper():
            tmp: str = chr((ord(char) + ord("A") - 3) % 26 + ord("A"))
            decrypted += tmp
        else:
            tmp: str = chr((ord(char) + ord("A")+3) % 26 + ord("a"))
            decrypted += tmp
    return decrypted


def get_text() -> str:
    '''obtains user input'''
    text: str = str(input("Enter text: "))
    return text


def menu() -> None:
    '''menu for the program'''
    print("1- Encrypt Text")
    print("2- Decrypt Text")
    print("3- Exit")

    choice: int = int(input("> "))
    if choice == 1:
        plaintext = get_text()
        encrypted: str = encrypt(plaintext)
        print(encrypted)
        return

    if choice == 2:
        plaintext = get_text()
        decrypted: str = decrypt(plaintext)
        print(decrypted)
        return

    if choice == 3:
        print("[!] Exiting ...")
        sys.exit(0)

    else:
        print("[-] Error")


menu()
