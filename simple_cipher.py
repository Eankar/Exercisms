import string

class Cipher:

    

    def __init__(self, key=None):
        pass

    def encode(self, text):

        alphabet = list(string.ascii_lowercase)
        encrypted_string = ""
        encrypted_text = []

        for i in range(len(text)):
            if alphabet.index(text[i]) < 22:
                encrypted_text.append(alphabet[alphabet.index(text[i]) - 4])
            else:
                encrypted_text.append(alphabet[alphabet.index(text[i]) - 26 - 4])

        for i in encrypted_text:
            encrypted_string += i
            
        print(encrypted_string)
        return encrypted_string

    def decode(self, text):
        pass

    encode(1, "iamapandabear")