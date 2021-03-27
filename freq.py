# counting frequency of characters or bi/trigrams in given text
def frequencies(item, interval=1, case_sensitive=False, delimiter=" "):
    if type(interval) is not int or interval not in range(5):
        return False
    if case_sensitive is False:
        item = item.upper()
    freq_dict = {}
    if interval == 1:
        for char in item:
            if char in freq_dict.keys():
                freq_dict[char] += 1
            else:
                freq_dict[char] = 0
    else:
        for index in range(len(item)-interval):
            selected = item[index:index+interval]
            if delimiter not in selected:
                if selected in freq_dict.keys():
                    freq_dict[selected] += 1
                else:
                    freq_dict[selected] = 0
    return freq_dict


# count frequencies of characters for polyalphabetic ciphers (eg viegnere), ommiting every non-alpahbetic character
def poli_frequencies(item, interval, case_sensitive=False):
    if type(interval) is not int or interval < 2:
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
                freq_list[counter % interval][char] = 0
    return freq_list
