# simple monoalphabetic rotation cipher with integer as key, and optional reference alphabet (by default full upper
# latin) if reference alphabet is full lower/upper, ciphering will convert them both to same letter, but will keep
# capitalization
from pattern import MasterCipher

alph_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Caesar(MasterCipher):
    def __init__(self, enc_key, reference=alph_EN):
        try:
            enc_key = int(enc_key) % len(reference)
        except ValueError:
            assert enc_key.isnumeric()
        if reference.islower() or reference.isupper():
            ci_table = str.maketrans(reference.lower() + reference, reference.lower()[enc_key:] +
                                     reference.lower()[:enc_key] + reference[enc_key:] + reference[:enc_key])
            enc_key = -enc_key % len(reference)
            de_table = str.maketrans(reference.lower() + reference, reference.lower()[enc_key:] +
                                     reference.lower()[:enc_key] + reference[enc_key:] + reference[:enc_key])
        else:
            ci_table = str.maketrans(reference, reference[enc_key:] + reference[:enc_key])
            enc_key = -enc_key % len(reference)
            de_table = str.maketrans(reference, reference[enc_key:] + reference[:enc_key])
        self.cipher_key = ci_table
        self.decipher_key = de_table
        self.reference = reference

    def cipher(self, plain_text):
        return super().cipher(plain_text)

    def decipher(self, ciphered_text):
        return super().decipher(ciphered_text)


library = {"ROT13": [13],
           "ROT47": (47, ('!"#$%&\'()*+,-./0123456789:;<=>?'
                          '@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'))}

if __name__ == "__main__":
    asd = Caesar(*library["ROT13"])
    sad = Caesar(*library["ROT47"])
    print(asd.cipher("Chron pulk twoj i szesc flag"))
    print(sad.cipher("Chron pulk twoj i szesc flag"))
    print(asd.cipher("Pueba chyx gjbw v fmrfp synt"))
    print(sad.cipher("r9C@? AF=< EH@; : DK6D4 7=28"))
    print(asd.decipher("Pueba chyx gjbw v fmrfp synt"))
    print(sad.decipher("r9C@? AF=< EH@; : DK6D4 7=28"))
