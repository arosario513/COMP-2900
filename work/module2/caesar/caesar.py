'''caesar cipher class'''


class Caesar:
    '''has the cipher and decipher methods'''
    @staticmethod
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

    @staticmethod
    def decrypt(text: str) -> str:
        '''decodes cipher'''
        decrypted: str = ""
        for char in text:
            if char.isupper():
                tmp: str = chr((ord(char) + ord("A") - 3) % 26 + ord("A"))
                decrypted += tmp
            else:
                tmp: str = chr((ord(char) + 4) % 26 + ord("a"))
                decrypted += tmp
        return decrypted
