# cipher swapping letters in pairs, with builded-in key generator, forcing output to be same capitalization as input
# key should be even, non-repeating iterable object eg GADERYPOLUKI
from pattern import MasterCipher


class RevSubstitution(MasterCipher):
    def __init__(self, enc_key):
        assert len(enc_key) % 2 == 0
        trans_dict = {}
        for x in range(len(enc_key)//2):
            trans_dict[enc_key[x * 2].upper()] = enc_key[x * 2 + 1].upper()
            trans_dict[enc_key[x * 2 + 1].upper()] = enc_key[x * 2].upper()
            trans_dict[enc_key[x * 2].lower()] = enc_key[x * 2 + 1].lower()
            trans_dict[enc_key[x * 2 + 1].lower()] = enc_key[x * 2].lower()
        self.cipher_key = self.decipher_key = str.maketrans(trans_dict)

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
