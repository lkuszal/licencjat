# cipher swapping letters in pairs, with builded-in key generator, forcing output to be same capitalization as input

# key should be even, non-repeating iterable object eg GADERYPOLUKI
def correct(enc_key):
    try:
        iter(enc_key)
        if len(enc_key) % 2 == 0:
            return True
    except TypeError:
        return False


def cipher(text, enc_key):
    if correct(enc_key) is False:
        return False
    tr_tab = key_generator(enc_key)
    return text.translate(tr_tab)


# self reversible cipher, so double encryption returns plain text
def decipher(text, enc_key):
    return cipher(text, enc_key)


# returns maketrans dictionary for self-reversible substitution (de)ciphering, doesn't change capitalization of text
def key_generator(key):
    trans_dict = {}
    for x in range(len(key) // 2):
        trans_dict[key[x * 2].upper()] = key[x * 2 + 1].upper()
        trans_dict[key[x * 2 + 1].upper()] = key[x * 2].upper()
        trans_dict[key[x * 2].lower()] = key[x * 2 + 1].lower()
        trans_dict[key[x * 2 + 1].lower()] = key[x * 2].lower()
    result = str.maketrans(trans_dict)
    print(type(result))
    return result


if __name__ == "__main__":
    a = "Chroń pułk twój i sześć flag"
    print(cipher(a, "GADERYPOLUKI"))
