from vigenere_tools import caesar_solver, length_by_kappa_solver, poli_lists
from collection import alph_EN
from vigenere_tester import vigenere_generator
from freq import poli_frequencies
from fitting import fitter, lang_checker
from vigenere import Vigenere


def cracker(lenght, key_length, sample):
    good_ones = []
    bad_ones = []
    for n in range(sample):
        text, master_key = vigenere_generator(lenght, key_length)
        for length in length_by_kappa_solver(text):
            key = ""
            for x in poli_lists(poli_frequencies(text, length)):
                #key += alph_EN[caesar_solver(x)]
                print(caesar_solver(x))
            asd = Vigenere(key)
            plaintext = asd.decipher(text)
            if key == master_key or key*2 == master_key:
                
                good_ones.append(fitter(plaintext))
            else:
                bad_ones.append(fitter(plaintext))
    return [good_ones, bad_ones]


if __name__ == "__main__":
    print(cracker(100, 2, 1))
