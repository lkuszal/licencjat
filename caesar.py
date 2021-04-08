# simple monoalphabetic rotation cipher with integer as key, and optional reference alphabet (by default full upper
# latin) if reference alphabet is full lower/upper, ciphering will convert them both to same letter, but will keep
# capitalization
alph_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# key should be an integer, while
def correct(enc_key):
    if type(enc_key) is int:
        return True
    return False


def cipher(text, enc_key, reference=alph_EN):
    if not correct(enc_key):
        return False
    enc_key = int(enc_key) % len(reference)
    if reference.islower() or reference.isupper():
        table = str.maketrans(reference.lower() + reference, reference.lower()[enc_key:] +
                              reference.lower()[:enc_key] + reference[enc_key:] + reference[:enc_key])
    else:
        table = str.maketrans(reference, reference[enc_key:]+reference[:enc_key])
    output = text.translate(table)
    return output


def decipher(text, enc_key, reference=alph_EN):
    return cipher(text, -enc_key, reference)


library = {"ROT13": [13],
           "ROT47": (47, ('!"#$%&\'()*+,-./0123456789:;<=>?'
                          '@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'))}

if __name__ == "__main__":
    print(cipher("Chron pulk twoj i szesc flag", 11))
    print(decipher("Nsczy afwv ehzu t dkpdn qwlr", 11))
    print(cipher("Chron pulk twoj i szesc flag", *library["ROT47"]))
    print(cipher("puebachyxgjbwvfmrfpsyntv", *library["ROT13"]))
