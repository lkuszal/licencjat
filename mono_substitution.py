# substitution cipher, where every letter is replaced by another one, or some symbol (but length of one),
# not supporting differences between capitalzations

# key should be full, converted alphabet same length as reference vector
def correct(enc_key, reference):
    try:
        iter(enc_key)
        if all(len(x) == 1 for x in enc_key) and len(enc_key) == len(reference):
            return True
    except TypeError:
        pass
    return False


def cipher(text, enc_key, reference='ABCDEFGHIJKLMNOPQRTUVWXYZ'):
    if correct(enc_key, reference) is False:
        return False
    tr_tab = key_generator(reference, enc_key)
    return text.translate(tr_tab)


def decipher(text, enc_key, reference='ABCDEFGHIJKLMNOPQRTUVWXYZ'):
    if correct(enc_key, reference) is False:
        return False
    tr_tab = key_generator(enc_key, reference)
    return text.translate(tr_tab)


# returns maketrans dictionary for full, non-self-reversible substitutions, as key you should pass full
# converted alphabet (iterable) and refferencing, same-length full alphabet
def key_generator(*args):
    trans_dict = {}
    for x, y in zip(args):
        if x != y:
            trans_dict[y.lower()] = x.lower()
            trans_dict[y.upper()] = x.upper()
    return str.maketrans(trans_dict)


library = {"A1Z26": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                     '18', '19', '20', '21', '22', '23', '24', '25', '26']}


if __name__ == "__main__":
    pass
