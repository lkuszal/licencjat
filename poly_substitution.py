from random import choice
from collection import alph_EN
from pattern import MasterCipher


class PolySubstitution(MasterCipher):
    """substitution cipher where every letter of suppresed text is replaced by some string (usually choosen by
    randomly choosed from few options), but every string has to be unique between letter's collections"""
    def __init__(self, enc_key, reference=alph_EN, delimeter=None, const_len=None, space=" "):
        unnested_key = [x for y in enc_key for x in y]
        assert len(unnested_key) == len(set(unnested_key))
        assert (delimeter is None) != (const_len is None)
        assert len(enc_key) == len(reference)
        self.delimeter = delimeter
        if const_len is not None:
            try:
                const_len = int(const_len)
            except ValueError:
                assert const_len.isnumeric()
            assert len(set([len(x) for x in unnested_key])) == 1
            self.const_len = const_len
        assert (delimeter != "") or (const_len != str(0))
        enc_dict = {}
        dec_dict = {}
        for x, y in zip(reference.upper(), enc_key):
            enc_dict[x] = y
            for z in y:
                dec_dict[z] = x
        self.cipher_key = enc_dict
        self.decipher_key = dec_dict
        self.space = space
        
    def cipher(self, plain_text):
        output = ""
        if self.delimeter is None:
            appendix = ""
        else:
            appendix = self.delimeter
        for word in plain_text.split():
            for char in word:
                if char in self.cipher_key:
                    output += choice(self.cipher_key[char]) + appendix
                output += self.space
        return output
    
    def decipher(self, ciphered_text):
        output = ""
        if self.space != "":
            if self.delimeter is not None:
                for word in ciphered_text.split(self.space):
                    for char in word.split(self.delimeter):
                        output += self.decipher_key[char]
                    output += " "
            else:
                for word in ciphered_text.split(self.space):
                    for x in range(0, len(ciphered_text), self.const_len):
                        output += self.decipher_key[word[x:x+self.const_len]]
        else:
            if self.delimeter is not None:
                for char in ciphered_text.split(self.delimeter):
                    output += self.decipher_key[char]
            else:
                for x in range(0, len(ciphered_text), self.const_len):
                    output += self.decipher_key[ciphered_text[x:x+self.const_len]]
        return output
        
        
def key_generator_karolinka(item):
    """additional function to generate karolinka-like cipher keys"""
    table = [[] for x in range(len(alph_EN))]
    for x in range(len(item)):
        for y in range(len(item)):
            table[alph_EN.index((chr(((ord(item.upper()[x]) - 65 + y) % 26) + 65)))].append(str(x + 1) + str(y + 1))
    return table


library = {"karolinka": [key_generator_karolinka("KAROLINKA"), alph_EN, None, 2]}
# testing
if __name__ == "__main__":
    karolinka = PolySubstitution(*library["karolinka"])
    print(karolinka.cipher("CHRONPULKTWOJISZESCFLAG"))
    print(karolinka.decipher("2398574114163482115949726229323925452396649197"))
