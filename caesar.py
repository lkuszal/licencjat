# simple monoalphabetic rotation cipher with natural number as key
# TOO SLOW, SUCCEEDED BY CAESAR_TRANS

def correct(enc_key):
    if enc_key.isdigit():
        return True
    return False


def cipher(text, enc_key):
    if not correct(enc_key):
        return False
    output = ""
    enc_key = int(enc_key)
    for ch in text:
        if 64 < ord(ch) < 91:
            output += chr((enc_key + ord(ch) - 65) % 26 + 65)
        elif 96 < ord(ch) < 123:
            output += chr((enc_key + ord(ch) - 97) % 26 + 97)
        else:
            output += ch
    return output


def decipher(text, enc_key):
    if not correct(enc_key):
        return False
    output = ""
    enc_key = int(enc_key)
    for ch in text:
        if 64 < ord(ch) < 91:
            output += chr((-enc_key + ord(ch) - 65) % 26 + 65)
        elif 96 < ord(ch) < 123:
            output += chr((-enc_key + ord(ch) - 97) % 26 + 97)
        else:
            output += ch
    return output
    
    
if __name__ == "__main__":
    print(cipher("Chron pulk twoj i szesc flag", "13"))
    print(decipher("Pueba chyx gjbw v fmrfp synt", "13"))
