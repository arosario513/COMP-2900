'''menu'''

import sys
from caesar import Caesar


class Menu:
    '''menu class'''

    def __get_text(self) -> str:
        '''obtains user input'''
        text: str = str(input("Enter text: "))
        return text

    def run(self) -> None:
        '''menu for the program'''
        while True:
            print("1- Encrypt Text")
            print("2- Decrypt Text")
            print("3- Exit")
            choice: int = int(input("> "))

            if choice == 1:
                plaintext = self.__get_text()
                encrypted: str = Caesar.encrypt(plaintext)
                print(f"Ciphered Text: {encrypted}")

            elif choice == 2:
                plaintext = self.__get_text()
                decrypted: str = Caesar.decrypt(plaintext)
                print(f"Deciphered Text: {decrypted}")

            elif choice == 3:
                print("[!] Exiting ...")
                sys.exit(0)

            else:
                print("[-] Error")
