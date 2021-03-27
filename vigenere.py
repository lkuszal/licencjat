# Polyalphabetic rotating cipher with key in latin alphabet format

def correct(enc_key):
    for char in enc_key.upper():
        if not 64 < ord(char) < 91:
            return False
    return True


def cipher(text, enc_key):
    if not correct(enc_key):
        return False
    output = ""
    n = 0
    enc_key = enc_key.upper()
    for ch in text:
        if 64 < ord(ch) < 91:
            output += chr((ord(enc_key[n % len(enc_key)]) - 65 + ord(ch) - 65) % 26 + 65)
            n += 1
        elif 96 < ord(ch) < 123:
            output += chr((ord(enc_key[n % len(enc_key)]) - 65 + ord(ch) - 97) % 26 + 97)
            n += 1
        else:
            output += ch
    return output


def decipher(text, enc_key):
    if not correct(enc_key):
        return False
    output = ""
    n = 0
    enc_key = enc_key.upper()
    for ch in text:
        if 64 < ord(ch) < 91:
            output += chr((-ord(enc_key[n % len(enc_key)]) + 65 + ord(ch) - 65) % 26 + 65)
            n += 1
        elif 96 < ord(ch) < 123:
            output += chr((-ord(enc_key[n % len(enc_key)]) + 65 + ord(ch) - 97) % 26 + 97)
            n += 1
        else:
            output += ch
    return output


if __name__ == "__main__":
    print(cipher("Chron pulk twoj i szesc flag", "key"))
    print(decipher("Mlpyr nepi damt m qjiqm jjkk", "key"))
