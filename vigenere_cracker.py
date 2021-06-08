from vigenere_tools import caesar_solver, length_by_kappa_solver, poli_lists, chis_scrap
from vigenere_tester import vigenere_generator
from freq import poli_frequencies
from vigenere import Vigenere
from language_variables import alphabet_list
from solutions_checker import solutions_checker


def vigenere_solver(text):
    results = []
    for length in length_by_kappa_solver(text):
        chis = []
        for x in poli_lists(poli_frequencies(text, length)):
            temp = []
            for y in caesar_solver(x):
                temp.append([y[0], alphabet_list[y[1]]])
            chis.append(temp)
        results.extend(chis_scrap(chis))
    results = [x[1] for x in results]
    print(results)
    return solutions_checker(text, Vigenere, results)
    
    
if __name__ == "__main__":
    print(vigenere_solver(vigenere_generator(100, 7)[0]))
