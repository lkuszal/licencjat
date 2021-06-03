from ciphers.pattern import MasterCipher


# cipher swapping letters in given pairs (so requiring to be even-length) as unique letter string
class RevSubstitution(MasterCipher):
    # creating string maketrans dicts to swap letters. Either converting both letters same way, keeping capitalization
    # or treating them differently
    def __init__(self, enc_key):
        assert len(enc_key) % 2 == 0
        trans_dict = {}
        if enc_key.isupper() or enc_key.islower():
            for x in range(len(enc_key)//2):
                trans_dict[enc_key[x * 2].upper()] = enc_key[x * 2 + 1].upper()
                trans_dict[enc_key[x * 2 + 1].upper()] = enc_key[x * 2].upper()
                trans_dict[enc_key[x * 2].lower()] = enc_key[x * 2 + 1].lower()
                trans_dict[enc_key[x * 2 + 1].lower()] = enc_key[x * 2].lower()
        else:
            for x in range(len(enc_key)//2):
                trans_dict[enc_key[x * 2]] = enc_key[x * 2 + 1]
                trans_dict[enc_key[x * 2 + 1]] = enc_key[x * 2]
        self.cipher_key = self.decipher_key = str.maketrans(trans_dict)

    # cipher and decipher methodes use both same method from abc MasterCipher, by simply using string .translate method
    def cipher(self, plain_text):
        return super().cipher(plain_text)

    def decipher(self, ciphered_text):
        return super().decipher(ciphered_text)


library = {'BAWOLETYKIJU': 'BAWOLETYKIJU', 'BITWAOCHMURY': 'BITWAOCHMURY', 'DIAMENTOWYUL': 'DIAMENTOWYUL',
           'GADERYPOLUKI': 'GADERYPOLUKI', 'GUBIKALESONYHALOJUPITERY': 'GUBIKALESONYHALOJUPITERY',
           'KACEMINUTOWY': 'KACEMINUTOWY', 'KONIECMATURY': 'KONIECMATURY', 'MALINOWEBUTY': 'MALINOWEBUTY',
           'MOTYLECUDAKI': 'MOTYLECUDAKI', 'NOWEBUTYLISA': 'NOWEBUTYLISA', 'POLITYKARENU': 'POLITYKARENU',
           'REGULAMINOWY': 'REGULAMINOWY', 'TALERZBIGOSU': 'TALERZBIGOSU'}


if __name__ == "__main__":
    asd = RevSubstitution(library["GADERYPOLUKI"])
    print(asd.cipher("Chron pulk twoj i szesc flag"))
    print(asd.decipher("Chypn olui twpj k szdsc fuga"))
