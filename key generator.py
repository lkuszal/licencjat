# creating various encryption key-objects; temporary collection, further to be include in specific files
alphabet_EN = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_PL = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
               'S', 'T', 'U', 'W', 'Y', 'Z']


# returns maketrans dictionary for self-reversible substitution (de)ciphering, as key you should pass
# string like "GADERYPOLUKI"
def rev_subst(key):
    trans_dict = {}
    for x in range(len(key) // 2):
        trans_dict[key[x * 2].upper()] = key[x * 2 + 1].upper()
        trans_dict[key[x * 2 + 1].upper()] = key[x * 2].upper()
        trans_dict[key[x * 2].lower()] = key[x * 2 + 1].lower()
        trans_dict[key[x * 2 + 1].lower()] = key[x * 2].lower()
    result = str.maketrans(trans_dict)
    print(type(result))
    return result


# returns maketrans dictionary for full, non-self-reversible substitutions, as key you should pass full
# converted alphabet (iterable) and refferencing, same-length full alphabet
def full_subst(key, reference=alphabet_EN):
    assert len(key) == len(reference)
    trans_dict = {}
    for x, y in zip(key, reference):
        if x != y:
            trans_dict[y.lower()] = x.lower()
            trans_dict[y.upper()] = x.upper()
    result = str.maketrans(trans_dict)
    return result


if __name__ == "__main__":
    a = rev_subst("GADERYPOLUKI")
    b = "Chroń pułk twój i sześć flag"
    print(b.translate(a))
