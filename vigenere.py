from pattern import MasterCipher


# Polyalphabetic rotating cipher (caesar like) with key in latin alphabet format, where letters are denotating
# rotation shift and position of ciphered letter correspond to some letter of key, as modulo of length of key
class Vigenere(MasterCipher):
    def __init__(self, enc_key):
        # simple checking and conversion of key to upper capitalization
        assert enc_key.isalpha()
        self.cipher_key = enc_key.upper()
        self.decipher_key = enc_key.upper()

    # rotates iterated letter by shift value of corresponding key letter. value of letter and rotation is based on
    # ord and chr functions, which allow to keep capitalization of letter
    def cipher(self, plain_text):
        output = ''
        n = 0
        for ch in plain_text:
            if 64 < ord(ch) < 91:
                output += chr((ord(self.cipher_key[n % len(self.cipher_key)]) - 65 + ord(ch) - 65) % 26 + 65)
                n += 1
            elif 96 < ord(ch) < 123:
                output += chr((ord(self.cipher_key[n % len(self.cipher_key)]) - 65 + ord(ch) - 97) % 26 + 97)
                n += 1
            else:
                output += ch
        return output

    # deciphering is based on same method, with difference, that key value is substracted instead of added to
    # letter value
    def decipher(self, ciphered_text):
        output = ""
        n = 0
        for ch in ciphered_text:
            if 64 < ord(ch) < 91:
                output += chr((-ord(self.decipher_key[n % len(self.decipher_key)]) + 65 + ord(ch) - 65) % 26 + 65)
                n += 1
            elif 96 < ord(ch) < 123:
                output += chr((-ord(self.decipher_key[n % len(self.decipher_key)]) + 65 + ord(ch) - 97) % 26 + 97)
                n += 1
            else:
                output += ch
        return output


library = {}


if __name__ == "__main__":
    asd = Vigenere("key")
    print(asd.cipher("Chron pulk twoj i szesc flag"))
    print(asd.decipher("Mlpyr nepi damt m qjiqm jjkk"))
