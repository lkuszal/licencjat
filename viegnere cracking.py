import freq
import vigenere
from collection import PL_freq, alph_EN

def cracker(text, language_freq=PL_freq):
    pass


def chi_squre(observed, expected):
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
    results = []
    for x in freq_lists:
        temp = []
        for y in alph_EN:
            temp.append(x.get(y, 0))
        results.append(temp)
    return results


if __name__ == "__main__":
    
