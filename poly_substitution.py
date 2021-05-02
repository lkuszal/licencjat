# substitution cipher where every letter of suppresed text is replaced by some string (usually choosen by
# randomly choosed from few options), but every string has to be unique between letter's collections
from random import choice
from collection import alph_EN
from pattern import MasterCipher


class PolySubstitution(MasterCipher):
    def __init__(self, enc_key, reference=alph_EN, delimeter=None, const_len=None):
        assert len(enc_key) == len(reference)
        unnested_key = [x for y in enc_key for x in y]
        assert len(unnested_key) == len(set(unnested_key))
        assert (delimeter is None) != (const_len is None)
        assert set([type(x) for x in enc_key]) == {list}
        if const_len is not None:
            assert const_len.isnumeric()
            const_len = int(const_len)
            assert {len(x) for x in unnested_key} == {const_len}
        trans_dict_en = {}
        trans_dict_de = {}
        for x, y in zip(reference.upper(), enc_key):
            trans_dict_en[x] = y
            for z in y:
                trans_dict_de[z] = x
        self.cipher_key = trans_dict_en
        self.decipher_key = trans_dict_de
        self.reference = reference
        self.delimeter = delimeter
        self.const_len = const_len

    def cipher(self, plain_text):
        output = ''
        if self.delimeter is None:
            for char in plain_text:
                if char in self.cipher_key.keys():
                    output += choice(self.cipher_key[char])
                elif char == " ":
                    output += char
        else:
            for char in plain_text:
                if char in self.cipher_key.keys():
                    output += choice(self.cipher_key[char])
                else:
                    output += char
                output += self.delimeter
        return output

    def decipher(self, ciphered_text):
        output = ''
        if self.delimeter is None:
            for word in ciphered_text.split():
                for x in range(len(word)//self.const_len):
                    piece = word[self.const_len*x:self.const_len*x+self.const_len]
                    if piece in self.decipher_key.keys():
                        output += self.decipher_key[piece]
                output += " "
        else:
            for word in ciphered_text.split():
                for char in word.split(self.delimeter):
                    if char in self.decipher_key.keys():
                        output += self.decipher_key[char]
                    else:
                        output += char
                output += " "
        return  output


def key_generator_karolinka(item):
    table = [[] for x in range(len(alph_EN))]
    for x in range(len(item)):
        for y in range(len(item)):
            table[alph_EN.index((chr(((ord(item.upper()[x]) - 65 + y) % 26) + 65)))].append(str(x + 1) + str(y + 1))
    return table


# dictionary containing frequently used keys, or empty one, in case of passing additional argument to function,
# whole value should be collected as a tuple
library = {"karolinka": [key_generator_karolinka("KAROLINKA"), alph_EN, None, "2"]}

# testing
if __name__ == "__main__":
    sad = PolySubstitution(*library["karolinka"])
    print(sad.cipher("CHRONPULKTWOJISZESCFLAG"))
    print(sad.decipher("2398574114163482115949726229323925452396649197"))
