# Written by Lukasz Cholodecki as part of 2021 thesis
from fitting import lang_checker


def solutions_checker(text, cipher_object, results, outcomes=5):
    """function that tries to rate goodness of fittness of given texts to a language model, returning either false or
    true as result, depending wheter texts has been classified as correct and sorted by goodness of fit results"""
    approved = []
    mismatched = []
    for x in sorted(results[:outcomes]):
        ciphrogram = cipher_object(x)
        deciphered_text = ciphrogram.decipher(text)
        diff = lang_checker(deciphered_text)
        if diff == 0:
            approved.append([x, deciphered_text])
        else:
            mismatched.append([diff, [x, deciphered_text]])
    if approved:
        return True, approved
    else:
        a = [x[1] for x in sorted(mismatched)]
        return False, a
