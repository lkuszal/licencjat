import freq
from collection import PL_freq, alph_EN
from vigenere_tester import vigenere_generator
from statistics import mean


def cracker(text, language_freq=PL_freq):
    pass


def chi_square(observed, expected):
    assert len(observed) == len(expected)
    value = 0
    length_factor = sum(observed)
    value_other = 0
    expected_other = 0
    for o, e in zip(observed, expected):
        e *= length_factor
        if o < 5:
        # if True:
            value += (o-e)**2/e
        else:
            assert expected != 0
            value_other += o
            expected_other += e
    if value_other != 0:
        value += (value_other-expected_other)**2/expected_other
    return value


def poli_lists(freq_lists):
    results = []
    for x in freq_lists:
        temp = []
        for y in alph_EN:
            temp.append(x.get(y, 0))
        results.append(temp)
    return results


def cycle_list(input_list):
    return input_list[1:]+[input_list[0]]


def square_kappa_difference(kappa_list, kappa=0.05924):
    for x, y in enumerate(kappa_list):
        kappa_list[x] = (y-kappa)**2
    return kappa_list


def indexing_kappa(kappa_list):
    result = []
    while set(kappa_list) != {1}:
        min_val = kappa_list[0]
        min_index = 0
        for x, y in enumerate(kappa_list):
            if y < min_val:
                min_val = y
                min_index = x
        result.append(min_index+2)
        kappa_list[min_index] = 1
    return result


def caesar_solver(freq_list, reference=PL_freq):
    solutions = []
    for x in range(len(freq_list)):
        solutions.append(chi_square(freq_list, reference))
        freq_list = cycle_list(freq_list)
    return solutions.index(min(solutions))


def length_by_kappa_solver(text, limit=10):
    kappa_for_dif_len = []
    for x in range(2, limit+1):
        temp = []
        for y in freq.poli_frequencies(text, x):
            temp.append(freq.kappa_count(y))
        kappa_for_dif_len.append(mean(temp))
    return indexing_kappa(square_kappa_difference(kappa_for_dif_len))
    

if __name__ == "__main__":
    pass
    random_cryptotext = vigenere_generator(102, 4)
    print(length_by_kappa_solver(random_cryptotext[0]))
    print(random_cryptotext[1])
    results = []
    for x in poli_lists(freq.poli_frequencies(random_cryptotext[0], 4)):
        results.append(caesar_solver(x))
    a = ''
    for x in results:
        a += alph_EN[x]
    print(a)
