# key should be an iterable object, consisting only alphabetic characters
def correct(enc_key):
    try:
        if all(type(x) is str and x.isalpha() for x in enc_key):
            return True
        return False
    except TypeError:
        return False


# item needs to be formated as clean string, consisting only alphabetic characters from english alphabet
def cipher(item, enc_key, encryption=False):
    if correct(enc_key) is False or not item.isalpha():
        return False
    key_matrice = key_generator(enc_key)
    if key_matrice is False:
        return False
    if encryption is True:
        e = -1
    else:
        e = 1
    item = item.upper().replace("J", "I")
    output = ''
    bigram = ''
    for x in item:
        if len(bigram) == 0:
            bigram += x
        elif bigram[0] != x:
            bigram += x
            output += convert(bigram, key_matrice, e)
            bigram = ''
        else:
            bigram += "X"
            output += convert(bigram, key_matrice, e)
            bigram = x
    if len(bigram) == 1:
        bigram += "X"
        output += convert(bigram, key_matrice, e)
    return output
    
    
def decipher(item, enc_key):
    return cipher(item, enc_key, encryption=True)


# converts bigram, whether as encryption or decryption, based on value of e,
def convert(bigram, table, e):
    a = table.index(bigram[0])
    b = table.index(bigram[1])
    a_x, a_y = a//5, a % 5
    b_x, b_y = b//5, b % 5
    if a_x == b_x:
        return table[a_x*5+(a_y+e) % 5]+table[b_x*5+(b_y+e) % 5]
    elif a_y == b_y:
        return table[((a_x+e) % 5)*5+a_y]+table[((b_x+e) % 5)*5+b_y]
    else:
        return table[a_x*5+b_y]+table[b_x*5+a_y]


# returns list consisting full english alphabet in given order
def key_generator(key):
    unique = []
    for x in key.upper().replace("J", "I"):
        if x not in unique:
            unique.append(x)
    alph = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for x in alph:
        if x not in unique:
            unique.append(x)
    if len(unique) != 25:
        return False
    return unique


library = {}


if __name__ == "__main__":
    print(cipher("chronpulktwojiszescflagi", "WYKLUCZENIE"))
    print(decipher("ARTHFVWUEKKHGUZXENRZPNBAGU", "WYKLUCZENIE"))
