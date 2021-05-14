# substitution cipher where every letter of suppresed text is replaced by some string (usually choosen by
# randomly choosed from few options), but every string has to be unique between letter's collections
from random import choice
from collection import alph_EN


# key should be double nested list consisting all unique strings, length of reference alphabet, delimeter
def correct(enc_key, reference, delimeter, const_len):
    try:
        iter(reference)
        if set([type(x) for x in enc_key]) == {list}:
            if len(enc_key) == len(reference):
                unnested = [x for y in enc_key for x in y]
                if len(unnested) == len(set(unnested)):
                    # checking wheter keys strings are same length, or delimeter is passed
                    if (delimeter is None) != (const_len is None):
                        if type(const_len) is int:
                            if (set([len(x) for x in unnested])) == {const_len}:
                                return True
                        elif type(delimeter) is str:
                            return True
    except TypeError:
        pass
    return False


# method for cipher
def cipher(text, enc_key, reference=alph_EN, delimiter=None, const_len=None, **read_dict):
    if not correct(enc_key, reference, delimiter, const_len) or not text.isalpha():
        return False
    trans_dict = {}
    for x, y in zip(reference.upper(), enc_key):
        trans_dict[x] = y
    output = ''
    if delimiter is not None:
        for char in text:
            if char in trans_dict.keys():
                output += choice(trans_dict[char]) + delimiter
            else:
                return False
    else:
        for char in text:
            if char in trans_dict.keys():
                print(choice(trans_dict[char]))
                output += choice(trans_dict[char])
            else:
                return False
    return output


# method for decipher
def decipher(text, enc_key, reference=alph_EN, delimeter=None, const_len=None):
    if not correct(enc_key, reference, delimeter, const_len):
        return False
    trans_dict = {}
    for x, y in zip(enc_key, reference.upper()):
        for z in x:
            trans_dict[z] = y
    if delimeter is not None:
        text = text.split(delimeter)
        return "".join([trans_dict[word] for word in text])
    else:
        output = ''
        for x in range(0, len(text), const_len):
            output += trans_dict[text[x:x + const_len]]
        return output


def key_generator_karolinka(item):
    table = [[] for x in range(len(alph_EN))]
    for x in range(len(item)):
        for y in range(len(item)):
            table[alph_EN.index((chr(((ord(item.upper()[x]) - 65 + y) % 26) + 65)))].append(str(x + 1) + str(y + 1))
    return table


# dictionary containing frequently used keys, or empty one, in case of passing additional argument to function,
# whole value should be collected as a tuple
library = {"karolinka": [key_generator_karolinka("KAROLINKA"), alph_EN, None, 2]}

# testing
if __name__ == "__main__":
    print(key_generator_karolinka("karolinka"))
    print(cipher("CHRONPULKTWOJISZESCFLAG", *library["karolinka"]))
    print(decipher("2398574114163482115949726229323925452396649197", *library["karolinka"]))
