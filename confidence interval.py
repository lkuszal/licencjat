from vigenere_tools import caesar_solver, length_by_kappa_solver, poli_lists, chis_scrap
from vigenere_tester import vigenere_generator
from freq import poli_frequencies
from fitting import fitter
from vigenere import Vigenere
from collection import alph_EN


def fitter_cracker(lenght, key_length, sample):
    """solves random ciphering collecting frequency values for bad and good solvings (made for mass getting
    frequencies to set thresholds"""
    good_ones = []
    bad_ones = []
    results = []
    for n in range(sample):
        text, master_key = vigenere_generator(lenght, key_length)
        for length in length_by_kappa_solver(text):
            chis = []
            for x in poli_lists(poli_frequencies(text, length)):
                temp = []
                for y in caesar_solver(x):
                    temp.append([y[0],alph_EN[y[1]]])
                chis.append(temp)
        for x in chis_scrap(chis):
            vig_obj = Vigenere(x[1])
            plaintext = vig_obj.decipher(text)
            if x[1] == master_key or x[1] == master_key*2:
                good_ones.append(fitter(plaintext))
            else:
                bad_ones.append(fitter(plaintext))
    return good_ones, bad_ones


def confidence_2(length):
    """retuns possible tresholds for given alphas (in code) with values and fit percentages"""
    good, bad = fitter_cracker(length, 6, 1000)
    good_stats = [[] for x in range(12)]
    for x in good:
        for n, y in enumerate(x):
            good_stats[n].append(y)
    for x in good_stats:
        x.sort()
    bad_stats = [[] for x in range(12)]
    for x in bad:
        for n, y in enumerate(x):
            bad_stats[n].append(y)
    for x in bad_stats:
        x.sort()
    for x in range(len(good_stats)):
        for y in [0.95, 0.955, 0.96, 0.965, 0.97, 0.975, 0.98, 0.985, 0.99, 0.995, 1]:
            a = good_stats[x][int(y*len(good_stats[x])//1)-1]
            b = 0
            for z in bad_stats[x][::-1]:
                if z < a:
                    break
                b += 1
            print(y, a, (len(bad_stats[x])-b)/len(bad_stats[x]))

            
if __name__ == "__main__":
    print(fitter_cracker(1000, 5, 1))
