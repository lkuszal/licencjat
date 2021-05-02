# substitution cipher for key's symbols of different length than 1, e.g morse code. As arguments, should be passed
# encryption key, reference as alphabet, boolean indicating if lower and upper cases should be converted to same
from collection import alph_EN
from pattern import MasterCipher


class FullSubstitution(MasterCipher):
    def __init__(self, enc_key, reference=alph_EN, differental_capitalization=False, delimiter="", space=" "):
        assert len(enc_key) == len(reference)
        if differental_capitalization is False:
            enc_key *= 2
            reference = reference.lower() + reference.upper()
        trans_dict_de = {}
        trans_dict_en = {}
        for x, y in zip(enc_key, reference):
            trans_dict_en[y] = x
            trans_dict_de[x] = y
        self.cipher_key = trans_dict_en
        self.decipher_key = trans_dict_de
        self.delimiter = delimiter
        self.space = space

    def cipher(self, plain_text):
        output = ''
        for char in plain_text:
            if char in self.cipher_key.keys():
                output += self.cipher_key[char]
                output += self.delimiter
            elif char == " ":
                output += self.space
            else:
                output += char
                output += self.delimiter
        return output

    def decipher(self, ciphered_text):
        output = ''
        for word in ciphered_text.split(self.space):
            for char in word.split(self.delimiter):
                if char in self.decipher_key.keys():
                    output += self.decipher_key[char]
                else:
                    output += char
            output += " "
        return output


# every dict value should contain encryption key and other values if they are not default
library = {"Morse code": [['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                          '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'],
                          alph_EN, False, "/", " "],
           "multitap": [['2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7',
                        '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999'], alph_EN, False, ".", " "],
           "A1Z26": [[str(x) for x in range(1, 27)], alph_EN, False, " ", "  "],
           "A1Z23": [[str(x) for x in range(1, 24)], alph_EN]}


# testing
if __name__ == "__main__":
    asd = FullSubstitution(*library["Morse code"])
    print(asd.cipher("Chron pulk twoj i szesc flag"))
    print(asd.decipher("-.-./..../.-./---/-. .--./..-/.-../-.- -/.--/---/.--- .. .../--.././.../-.-. ..-./.-../.-/--."))
