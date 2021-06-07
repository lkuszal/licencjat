from vigenere_tools import caesar_solver, length_by_kappa_solver, poli_lists, chis_scrap
from vigenere_tester import vigenere_generator
from freq import poli_frequencies
from fitting import lang_checker
from vigenere import Vigenere
from collection import alph_EN


def vigenere_solver(text):
    results = []
    for length in length_by_kappa_solver(text):
        chis = []
        for x in poli_lists(poli_frequencies(text, length)):
            temp = []
            for y in caesar_solver(x):
                temp.append([y[0],alph_EN[y[1]]])
            chis.append(temp)
        results.extend(chis_scrap(chis))
    return solutions_checker(text, Vigenere, results)


def solutions_checker(text, cipher_object, results, outcomes=5):
    """magnum opus of library, from cipher_text returns most probable possibilites of solutions (as key and deciphered text)
    and also bool value - True if any solutions has been successful matched to language model or false and sorted 5 results
     by most probable, due to fittness to language model"""
    approved = []
    mismatched = []
    for x in sorted(results[:outcomes]):
        ciphrogram = cipher_object(x[1])
        deciphered_text = ciphrogram.decipher(text)
        diff = lang_checker(deciphered_text)
        if diff == 0:
            approved.append([x[1], deciphered_text])
        else:
            mismatched.append([diff, [x[1], deciphered_text]])
    if approved:
        return True, approved
    else:
        return False, sorted(mismatched)
        
        
if __name__ == "__main__":
    print(vigenere_solver(vigenere_generator(1000, 7)[0]))
