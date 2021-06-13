"""Polyalphabetic rotating cipher (caesar like) with key in latin alphabet format, where letters are denotating
rotation shift and position of ciphered letter correspond to some letter of key, as modulo of length of key"""
from pattern import MasterCipher
from language_variables import alphabet_list


class Vigenere(MasterCipher):
    def __init__(self, enc_key, alphabet=alphabet_list):
        # simple checking and conversion of key to upper capitalization
        assert enc_key.isalpha()
        self.cipher_key = enc_key.upper()
        self.decipher_key = enc_key.upper()
        self.key_length = len(self.cipher_key)
        self.alph = alphabet

    # rotates iterated letter by shift value of corresponding key letter. value of letter and rotation is based on
    # ord and chr functions, which allow to keep capitalization of letter
    def cipher(self, plain_text):
        lower_beg = ord(self.alph[0].lower())
        upper_beg = ord(self.alph[0].upper())
        alph_len = len(self.alph)
        output = ''
        n = 0
        for ch in plain_text:
            if ch.isalpha():
                if ch.isupper():
                    output += chr((ord(self.cipher_key[n % self.key_length]) - upper_beg + ord(ch) - upper_beg) %
                                  alph_len + upper_beg)
                    n += 1
                else:
                    output += chr((ord(self.cipher_key[n % self.key_length]) - upper_beg + ord(ch) - lower_beg) %
                                  alph_len + lower_beg)
                    n += 1
            else:
                output += ch
        return output

    # deciphering is based on same method, with difference, that key value is substracted instead of added to
    # letter value
    def decipher(self, ciphered_text):
        lower_beg = ord(self.alph[0].lower())
        upper_beg = ord(self.alph[0].upper())
        alph_len = len(self.alph)
        output = ''
        n = 0
        for ch in ciphered_text:
            if ch.isalpha():
                if ch.isupper():
                    output += chr((-ord(self.cipher_key[n % self.key_length]) + upper_beg + ord(ch) - upper_beg) % alph_len + upper_beg)
                    n += 1
                else:
                    output += chr((-ord(self.cipher_key[n % self.key_length]) + upper_beg + ord(ch) - lower_beg) % alph_len + lower_beg)
                    n += 1
            else:
                output += ch
        return output


library = {}


if __name__ == "__main__":
    asd = Vigenere("key")
    print(asd.cipher("Chron pulk twoj i szesc flag"))
    print(asd.decipher("Mlpyr nepi damt m qjiqm jjkk"))
    aaa = Vigenere("klucz")
    print(aaa.decipher("Mslqm zffm sgzd k rjpme evla"))
