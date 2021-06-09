from statistics import mean
import freq
from language_variables import letter_freq, alphabet_list, model_kappa
from collection import word_generator, normalise, suppress, random_text
from vigenere import Vigenere

def chi_square(observed, expected):
    """counts pearson chi square test between two list of counted occurances"""
    assert len(observed) == len(expected)
    value = 0
    length_factor = sum(observed)
    value_other = 0
    expected_other = 0
    for o, e in zip(observed, expected):
        e *= length_factor
        if o < 5:
            value += (o-e)**2/e
        else:
            assert expected != 0
            value_other += o
            expected_other += e
    if value_other != 0:
        value += (value_other-expected_other)**2/expected_other
    return value


def poli_lists(freq_lists):
    """converts list of dictionaries from freq.polifrequencies to nested list"""
    results = []
    for x in freq_lists:
        temp = []
        for y in alphabet_list:
            temp.append(x.get(y, 0))
        results.append(temp)
    return results


def cycle_list(input_list):
    """simply cut and paste first element of list on the end of it"""
    return input_list[1:]+[input_list[0]]


def square_kappa_difference(kappa_list, kappa=model_kappa):
    """counts mean square error versus given kappa in array and returns it as values list"""
    for x, y in enumerate(kappa_list):
        kappa_list[x] = (y-kappa)**2
    return kappa_list


def caesar_solver(freq_list, reference=letter_freq, results=2):
    """performs chi square test between two arrays, then cycle first one as long as checks all possibilites"""
    solutions = []
    for x in range(len(freq_list)):
        solutions.append([chi_square(freq_list, reference), x])
        freq_list = cycle_list(freq_list)
    return sorted(solutions)[:results]


def length_by_kappa_solver(text, limit=10, kappa=model_kappa):
    """counts mean kappa value of texts developed from division by every n-th letter with n from 2 to given limit"""
    kappa_for_dif_len = []
    for x in range(2, limit+1):
        temp = []
        for y in freq.poli_frequencies(text, x):
            temp.append(freq.kappa_count(y))
        kappa_for_dif_len.append(mean(temp))
    kappa_list = []
    for x, y in enumerate(kappa_for_dif_len):
        kappa_list.append([(y-kappa)**2, x+2])
    return [x[1] for x in sorted(kappa_list) if x[0] < 0.0001]
        

def chis_scrap(chis, options=3):
    results = []
    key = ''
    rate = []
    rate2 = []
    for x in range(len(chis)):
        key += chis[x][0][1]
        rate.append(chis[x][0][0])
        rate2.append(chis[x][1][0])
    results.append([mean(rate), key])
    diffs = []
    for n, x in enumerate(zip(rate, rate2)):
        diffs.append([abs(x[0]-x[1]), n])
    for x in sorted(diffs)[:options]:
        results.append([mean(rate[:x[1]]+[chis[x[1]][1][0]]+rate[x[1]+1:]), key[:x[1]]+chis[x[1]][1][1]+key[x[1]+1:]])
    return results
    
    
def vigenere_generator(length, key_length, supresssion=False):
    """returns text of given length (ciphered by random key of given length) and this key"""
    key = word_generator(key_length)
    text = normalise(random_text(length))
    if supresssion:
        text = suppress(text)
    asd = Vigenere(key)
    return asd.cipher(text), key
    
if __name__ == "__main__":
    pass
    random_cryptotext = vigenere_generator(200, 4)
    # print(length_by_kappa_solver(random_cryptotext[0]))
    # print(random_cryptotext[1])
    results = []
    for x in poli_lists(freq.poli_frequencies(random_cryptotext[0], 7)):
        # print(x)
        print(caesar_solver(x))
    # print(results)
