import numpy as np


def correct(enc_key):
    try:
        if all(type(x) is str and x.isalpha() for x in enc_key):
            return True
        return False
    except TypeError:
        return False


def cipher(text, enc_key):
    if correct(enc_key) is False:
        return False
    key_matrice = key_generator(enc_key)



# returns nested list 5x5
def key_generator(key):
    unique = []
    for x in key.upper().replace("J", "I"):
        if x not in unique:
            unique.append(x)
    alph = 'ABCDEFGHIKLMNOPQRTUVWXYZ'
    for x in alph:
        if x not in unique:
            unique.append(x)
    key_matrice = np.zeros((5, 5), dtype=str)
    for x in range(5):
        for y in range(5):
            key_matrice[x, y] = unique[5*x+y]
    # print(key_matrice)
    # shift = np.where(key_matrice == "A")
    # return np.roll(key_matrice, (-shift[0][0], -shift[1][0]))
    return key_matrice
