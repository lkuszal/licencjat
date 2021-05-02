# substitution cipher, where every letter is replaced by another one, or some symbol (but of length of one),
# not supporting differences between ciphering capitalzations, but keeping cases
from collection import alph_EN
from pattern import MasterCipher


class MonoSubstitution(MasterCipher):
    @super
    def __init__(self, enc_key, reference=alph_EN):
        assert len(enc_key) == len(reference)
        cipher_dict, decipher_dict = {}, {}
        for x, y in zip(enc_key, reference):
            if x != y:
                cipher_dict[y.lower()] = x.lower()
                cipher_dict[y.upper()] = x.upper()
                decipher_dict[y.lower()] = x.lower()
                decipher_dict[y.upper()] = x.upper()
        self.cipher_key = str.maketrans(cipher_dict)
        self.decipher_key = str.maketrans(decipher_dict)

    def cipher(self, plain_text):
        return plain_text.translate(self.cipher_key)

    def decipher(self, ciphered_text):
        return ciphered_text.translate(self.decipher_key)


library = {}


if __name__ == "__main__":
    sad = MonoSubstitution("NOPQRSTUVWXYZABCDEFGHIJKLM")
    asd = MonoSubstitution("NOPQRSTUVWXYZABCDEFGHIJKLM")
    print(hash(sad))
    print(hash(asd))
    print(sad.cipher("chron pulk twoj i szesc flag"))
    print(sad.decipher("pueba chyx gjbw v fmrfp synt"))
