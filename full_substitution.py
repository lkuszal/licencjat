from collection import alph_EN
from pattern import MasterCipher


# substitution cipher for key's symbols of different length than 1, e.g morse code. As arguments, should be passed
# encryption key, referencing alphabet, and delimeter seperating letters, and space seperating words
class FullSubstitution(MasterCipher):
    # creating encryption and decryption dictionaries from encryption keys and reference (same length)
    def __init__(self, enc_key, reference=alph_EN, delimiter="", space=" "):
        assert len(enc_key) == len(reference)
        assert delimiter != ''
        trans_dict_de = {}
        trans_dict_en = {}
        if reference.isupper() or reference.islower():
            for x, y in zip(enc_key, reference):
                trans_dict_en[y.lower()] = x.lower()
                trans_dict_en[y.upper()] = x.upper()
                trans_dict_de[x.lower()] = y.lower()
                trans_dict_de[x.upper()] = y.upper()
        else:
            for x, y in zip(enc_key, reference):
                trans_dict_en[y] = x
                trans_dict_de[x] = y
        self.cipher_key = trans_dict_en
        self.decipher_key = trans_dict_de
        self.delimiter = delimiter
        self.space = space

    # converting letters by encryption dictionary, adding delimiter between letters and space between words
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

    # spliting words first by space, then by delimeter, converting by decipher dictionary
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
                          alph_EN, "/", " "],
           "multitap": [['2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7',
                        '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999'], alph_EN, ".", " "],
           "A1Z26": [[str(x) for x in range(1, 27)], alph_EN, " ", "  "],
           "A1Z23": [[str(x) for x in range(1, 24)], alph_EN, " ", " "]}


# testing
if __name__ == "__main__":
    asd = FullSubstitution(*library["Morse code"])
    print(asd.cipher("Chron pulk twoj i szesc flag"))
    print(asd.decipher("-.-./..../.-./---/-. .--./..-/.-../-.- -/.--/---/.--- .. .../--.././.../-.-. ..-./.-../.-/--."))
