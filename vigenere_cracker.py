from vigenere_tools import caesar_solver, length_by_kappa_solver, poli_lists, chis_scrap
from vigenere_tester import vigenere_generator
from freq import poli_frequencies
from fitting import lang_checker
from vigenere import Vigenere


def vigenere_solver(text):
    """magnum opus of library, from text returns most probable possibilites of solutions (as key and deciphered text)
    and also bool value - True if any solutions has been successful matched to language model or false and sorted 5 results
     by most probable, due to fittness to language model"""
    results = []
    for length in length_by_kappa_solver(text):
        chis = []
        for x in poli_lists(poli_frequencies(text, length)):
            chis.append(caesar_solver(x))
        results.extend(chis_scrap(chis))
    approved = []
    mismatched = []
    for x in sorted(results[:5]):
        ciphrogram = Vigenere(x[1])
        deciphered_text = ciphrogram.decipher(text)
        diff = lang_checker(deciphered_text)
        if diff == 0:
            approved.append([x[1],deciphered_text])
        else:
            mismatched.append([diff, [x[1], deciphered_text]])
    if approved:
        return True, approved
    else:
        return False, sorted(mismatched)
        
        
if __name__ == "__main__":
    print(vigenere_solver(vigenere_generator(1000, 7)[0]))
