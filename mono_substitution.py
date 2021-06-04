"""substitution cipher, where every letter is replaced by another one, or some symbol (but length of one),
not supporting differences between ciphering capitalzations, but keeping cases"""
from collection import alph_EN
from pattern import MasterCipher


class MonoSubstitution(MasterCipher):
    """mono substitution aims to replace all selected letters or marks by any other letter or symbol, but length
    of one
    init method creates maketrans dicts containing all replacments, if reference contains only one capitalization
    f letters cipher will convert both lower and upper letters and keep their capitalization. Reference (english
    upper alphabet by default) and ciphered alphabet needs to be same of the same length"""
    def __init__(self, enc_key, reference=alph_EN):
        assert len(enc_key) == len(reference)
        cipher_dict, decipher_dict = {}, {}
        if reference.islower() or reference.isupper():
            for x, y in zip(enc_key, reference):
                if x != y:
                    cipher_dict[y.lower()] = x.lower()
                    cipher_dict[y.upper()] = x.upper()
                    decipher_dict[x.lower()] = y.lower()
                    decipher_dict[x.upper()] = y.upper()
        else:
            for x, y in zip(enc_key, reference):
                cipher_dict[y] = x
                decipher_dict[x] = y
        self.cipher_key = str.maketrans(cipher_dict)
        self.decipher_key = str.maketrans(decipher_dict)

    # cipher and decipher methodes use both same method from abc MasterCipher, by simply using string translate method
    def cipher(self, plain_text):
        return super().cipher(plain_text)

    def decipher(self, ciphered_text):
        return super().decipher(ciphered_text)


library = {"ROT13": ["NOPQRSTUVWXYZABCDEFGHIJKLM"]}


if __name__ == "__main__":
    sad = MonoSubstitution("NOPQRSTUVWXYZABCDEFGHIJKLM")
    asd = MonoSubstitution("NOPQRSTUVWXYZABCDEFGHIJKLM")
    print(sad.cipher("chron pulk twoj i szesc flag"))
    print(sad.decipher("pueba chyx gjbw v fmrfp synt"))
