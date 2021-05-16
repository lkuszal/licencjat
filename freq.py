# bunch of functions to examine text's properities connected with frequency, returning dictionary, or list of dicts

# counting frequency of characters or bi/trigrams in given text
def frequencies(item, interval=1, case_sensitive=False):
    assert type(interval) is int
    assert type(case_sensitive) is bool
    assert interval < 4
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
    assert type(interval) is int
    assert type(case_sensitive) is bool
    assert interval >= 2
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
            counter += 1
    return freq_list


# counts frequencies of substrings given length on word beginnings or endings
def words_edges_frequencies(item, length=3, beginning=True):
    assert type(length) is int
    assert length < 5
    assert type(beginning) is bool
    assert not str(item).isalpha()
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
    assert type(length) is int
    assert length < 5
    assert type(case_sensitive) is bool
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


# calculate kappa value (index of coincidence) of letter frequncies passed as dictionaries
def kappa_count(freq_dict):
    kappa_list = [freq_dict[x] for x in freq_dict.keys()]
    list_sum = sum(kappa_list)
    denominator = list_sum*(list_sum-1)
    kappa = 0
    for x in kappa_list:
        kappa += x*(x-1)/denominator
    return kappa


if __name__ == "__main__":
    pass
