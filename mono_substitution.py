# substitution cipher, where every letter is replaced by another one, or some symbol (but of length of one),
# not supporting differences between ciphering capitalzations, but keeping cases
from collection import alph_EN
from pa

# key should be full, converted alphabet same length as reference vector
def correct(enc_key, reference):
    try:
        iter(enc_key)
        if all(len(x) == 1 for x in enc_key) and len(enc_key) == len(reference):
            return True
    except TypeError:
        pass
    return False


def cipher(text, enc_key, reference=alph_EN):
    if correct(enc_key, reference) is False:
        return False
    tr_tab = key_generator(reference, enc_key)
    return text.translate(tr_tab)


def decipher(text, enc_key, reference=alph_EN):
    if correct(enc_key, reference) is False:
        return False
    tr_tab = key_generator(enc_key, reference)
    return text.translate(tr_tab)


# returns maketrans dictionary for full, non-self-reversible substitutions, as key you should pass full
# converted alphabet (iterable) and refferencing, same-length full alphabet
def key_generator(*args):
    trans_dict = {}
    for x, y in zip(*args):
        if x != y:
            trans_dict[y.lower()] = x.lower()
            trans_dict[y.upper()] = x.upper()
    return str.maketrans(trans_dict)


# if cipher uses different alphabet then both argument should be passed together in tuple
library = {}


if __name__ == "__main__":
    print(cipher("chronpulktwojiszescflag", "NOPQRSTUVWXYZABCDEFGHIJKLM"))
