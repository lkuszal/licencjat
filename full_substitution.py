# substitution cipher for key's symbols of different length than 1, e.g morse code. As arguments, should be passed
# encryption key, reference as alphabet, boolean indicating if lower and upper cases should be converted to same
alph_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# method ensuring that given key is in correct format
def correct(enc_key, reference):
    try:
        iter(enc_key)
        iter(reference)
        if len(enc_key) == len(reference):
            return True
    except TypeError:
        pass
    return False


# method for cipher
def cipher(text, enc_key, reference=alph_EN, repeat_capitalization=True, delimeter="", space=" "):
    if not correct(enc_key, reference):
        return False
    if repeat_capitalization is True:
        enc_key = enc_key*2
        reference = reference.upper() + reference.lower()
    trans_dict = key_generator(enc_key, reference)
    words_list_of_strings = text.split()
    words_list_of_lists = []
    for word in words_list_of_strings:
        new_word = []
        for char in word:
            if char in trans_dict.keys():
                char = trans_dict[char]
                # or by replace method?
            new_word.append(char)
        words_list_of_lists.append(new_word)
    output = []
    for word in words_list_of_lists:
        output.append(delimeter.join(word))
    return space.join(output)
    
    
# method for decipher, for selfreversing cipher call cipher function
def decipher(text, enc_key,  reference=alph_EN, repeat_capitalization=False, delimeter="", space=" "):
    if not correct(enc_key, reference):
        return False
    trans_dict = key_generator(reference, enc_key)
    words_list_of_strings = text.split(space)
    words_list_of_lists = []
    for word in words_list_of_strings:
        new_word = []
        word = word.split(delimeter)
        for char in word:
            if char in trans_dict.keys():
                char = trans_dict[char]
                # or by replace method?
            new_word.append(char)
        words_list_of_lists.append(new_word)
    output = []
    for word in words_list_of_lists:
        output.append("".join(word))
    return " ".join(output)


def key_generator(*args):
    trans_dict = {}
    for x, y in zip(*args):
        if x != y:
            trans_dict[y] = x
    return trans_dict


library = {"Morse code": [['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                          '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'],
                          alph_EN, True, "/", " "],
           "multitap": ['2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7',
                        '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999'],
           "A1Z26": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                     '18', '19', '20', '21', '22', '23', '24', '25', '26']}


# testing
if __name__ == "__main__":
    print(cipher("Chron pulk twoj i szesc flag", *library["Morse code"]))
    print(decipher("-.-./..../.-./---/-. .--./..-/.-../-.- -/.--/---/.--- .. .../--.././.../-.-. ..-./.-../.-/--.", *library["Morse code"]))
