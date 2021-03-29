# simple monoalphabetic rotation cipher with integer as key,
# and optional reference alphabet (by default full latin)
alph_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# key should be an integer, while
def correct(enc_key):
    if type(enc_key) is int:
        return True
    return False


def cipher(text, enc_key, reference=alph_EN):
    if not correct(enc_key):
        return False
    reference = reference.upper()
    enc_key = int(enc_key) % len(reference)
    table = str.maketrans(reference.lower() + reference, reference.lower()[enc_key:] +
                          reference.lower()[:enc_key] + reference[enc_key:] + reference[:enc_key])
    output = text.translate(table)
    return output


def decipher(text, enc_key, reference=alph_EN):
    return cipher(text, -enc_key, reference)


library = {"ROT13": 13}

if __name__ == "__main__":
    print(cipher("Chron pulk twoj i szesc flag", 11))
    print(decipher("Nsczy afwv ehzu t dkpdn qwlr", 11))
