from pattern import MasterCipher


class Playfair(MasterCipher):
    def __init__(self, enc_key):
        assert enc_key.isalpha()
        unique = []
        for x in enc_key.upper().replace("J", "I"):
            if x not in unique:
                unique.append(x)
        alph = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        for x in alph:
            if x not in unique:
                unique.append(x)
        assert len(unique) == 25
        self.cipher_key = unique
        self.decipher_key = unique

    def cipher(self, plain_text, e=1):
        plain_text = plain_text.upper().replace("J", "I")
        output = ''
        bigram = ''
        for x in plain_text:
            if x.isalpha():
                if len(bigram) == 0:
                    bigram += x
                elif bigram[0] != x:
                    bigram += x
                    output += self.convert(bigram, self.cipher_key, e)
                    bigram = ''
                else:
                    bigram += "X"
                    output += self.convert(bigram, self.cipher_key, e)
                    bigram = x
        if len(bigram) == 1:
            bigram += "X"
            output += self.convert(bigram, self.cipher_key, e)
        return output

    def decipher(self, ciphered_text):
        return self.cipher(ciphered_text, e=-1)

    def convert(self, bigram, table, e):
        a = table.index(bigram[0])
        b = table.index(bigram[1])
        a_x, a_y = a//5, a % 5
        b_x, b_y = b//5, b % 5
        if a_x == b_x:
            return table[a_x*5+(a_y+e) % 5]+table[b_x*5+(b_y+e) % 5]
        elif a_y == b_y:
            return table[((a_x+e) % 5)*5+a_y]+table[((b_x+e) % 5)*5+b_y]
        else:
            return table[a_x*5+b_y]+table[b_x*5+a_y]


library = {}

if __name__ == "__main__":
    asd = Playfair("Wykluczenie")
    print(asd.cipher("Chron pulk twoj i szesc flag"))
    print(asd.decipher("ARTHFVWUEKKHGUZXENRZPNBA"))
