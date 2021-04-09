# bunch of functions to examine text's properities connected with frequency, returning dictionary, or list of dicts

# counting frequency of characters or bi/trigrams in given text
def frequencies(item, interval=1, case_sensitive=False):
    if type(interval) is not int or interval not in range(5) or type(case_sensitive) is not bool:
        return False
    if case_sensitive is False:
        item = item.upper()
    freq_dict = {}
    if interval == 1:
        freq_dict = {key: item.count(key) for key in set(item)}
    else:
        for index in range(len(item)-interval):
            selected = item[index:index+interval]
            if selected.isalpha():
                if selected in freq_dict.keys():
                    freq_dict[selected] += 1
                else:
                    freq_dict[selected] = 1
    return freq_dict


# count frequencies of characters for polyalphabetic ciphers (eg viegnere), ommiting every non-alpahbetic character
def poli_frequencies(item, interval=2, case_sensitive=False):
    if type(interval) is not int or interval < 2 or type(case_sensitive) is not bool:
        return False
    freq_list = []
    if case_sensitive is False:
        item = item.upper()
    for n in range(interval):
        freq_list.append({})
    counter = 0
    for char in item:
        if char.isalpha():
            if char in freq_list[counter % interval].keys():
                freq_list[counter % interval][char] += 1
            else:
                freq_list[counter % interval][char] = 1
    return freq_list


# counts frequencies of substrings given length on word beginnings or endings
def words_edges_frequencies(item, length=3, beginning=True):
    if type(length) is not int or length not in range(1, 4) or type(beginning) is not bool:
        return False
    item = item.upper()
    freq_dict = {}
    word = ''
    for char in item:
        if char.isalpha():
            word += char
        else:
            if len(word) >= length:
                if beginning is True:
                    selected = word[:length]
                else:
                    selected = word[-length:]
                if selected in freq_dict.keys():
                    freq_dict[selected] += 1
                else:
                    freq_dict[selected] = 1
            word = ""
    return freq_dict


# counts frequencies of words of givien lengths
def short_words_frequencies(item, length=1, case_sensitive=False):
    if type(length) is not int or length not in range(1, 5) or type(case_sensitive) is not bool:
        return False
    if case_sensitive is False:
        item = item.upper()
    freq_dict = {}
    word = ""
    for char in item:
        if char.isalpha():
            word += char
        else:
            if len(word) == length:
                if word in freq_dict.keys():
                    freq_dict[word] += 1
                else:
                    freq_dict[word] = 1
            word = ''
    return freq_dict


if __name__ == "__main__":
    a = open("pt.txt", "r", encoding="utf8").read()
    print(frequencies(a))
    '''print(frequencies(a, interval=2))
    print(poli_frequencies(a))
    print(words_edges_frequencies(a, length=3))
    print(short_words_frequencies(a, length=4))'''
