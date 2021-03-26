# simple monoalphabetic rotation cipher with natural number as key
alph_L_EN = 'abcdefghijklmnopqrstuvwxyz'
alph_U_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def correct(enc_key):
    if enc_key.isdigit():
        return True
    return False


def cipher(text, enc_key):
    if not correct(enc_key):
        return False
    enc_key = int(enc_key) % len(alph_L_EN)
    table = str.maketrans(alph_L_EN + alph_U_EN, alph_L_EN[enc_key:] +
                          alph_L_EN[:enc_key] + alph_U_EN[enc_key:] + alph_U_EN[:enc_key])
    output = text.translate(table)
    return output


def decipher(text, enc_key):
    if not correct(enc_key):
        return False
    enc_key = int(enc_key) % len(alph_L_EN)
    table = str.maketrans(alph_L_EN[enc_key:] + alph_L_EN[:enc_key] +
                          alph_U_EN[enc_key:] + alph_U_EN[:enc_key], alph_L_EN + alph_U_EN)
    output = text.translate(table)
    return output


if __name__ == "__main__":
    print(cipher("Chron pulk twoj i szesc flag", "11"))
    print(decipher("Nsczy afwv ehzu t dkpdn qwlr", "11"))
