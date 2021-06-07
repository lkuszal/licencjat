from pattern import MasterCipher


# Playfair cipher aims to code text by bigrams, using table 5x5 containing whole alphabet (replacing J by I)
# in given order
class Playfair(MasterCipher):
    # cipher and decipher keys are the same, init method converts given string to one of length 25, containg all
    # unique letter, first from string, and then filled by not used letter from alphabet in order
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
        self.cipher_key = self.decipher_key = unique

    def cipher(self, plain_text, e=1):
        """cipher method converts all alphabetic characters to upper, deleting other ones. Passing not standard letter
        like language specific will raise an error - so whole text should be normalised before ciphering. Method divides
        whole text to two-letter length (bigram) and passing it to convert method, returning ciphered bigram"""
        plain_text = plain_text.upper().replace("J", "I")
        output = ''
        bigram = ''
        for x in plain_text:
            if x.isalpha():
                if len(bigram) == 0:
                    bigram += x
                elif bigram[0] != x:
                    bigram += x
                    output += self.convert(bigram, e)
                    bigram = ''
                else:
                    bigram += "X"
                    output += self.convert(bigram, e)
                    bigram = x
        if len(bigram) == 1:
            bigram += "X"
            output += self.convert(bigram, e)
        return output

    # decipher metod uses same code as cipher method, differing only by passing e-argument as -1 to convert method
    def decipher(self, ciphered_text):
        return self.cipher(ciphered_text, e=-1)

    def convert(self, bigram, e):
        """convert methods takes single bigram and e-argument telling whether code should be encoded (+1) or decoded (-1)
        Method virtualizes 5x5 matrix created from cipher_key (same as decipher_key) and finds coordinats of both letters
        from bigram by floor division and modulo (both of 5), and then, based on mutual placement of letters, returning
        converted bigram"""
        table = self.cipher_key
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
