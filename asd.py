'''
import freq
def dict_scrapper(freq_dict):
    key = []
    value = []
    counter = 0
    for x in sorted(freq_dict.keys()):
        counter += freq_dict[x]
        if freq_dict[x] > 20:
            key.append(x)
            value.append(freq_dict[x])
    print(counter, "\n", key, "\n", value)
    
    
if __name__ == "__main__":
    source_text = open("output_lines.txt", "r", encoding="utf-8")
    for x in range(1, 2):
        pass
        print(freq.frequencies(source_text.read(), x))
        # print(freq.poli_frequencies(corpus, 10))
        # dict_scrapper(freq.words_edges_frequencies(corpus, x, beginning=False))
        # dict_scrapper(freq.short_words_frequencies(corpus, x))
    # print(freq.kappa_count(freq.frequencies(corpus)))

asd = open("C:/Users/Latul/Desktop/asd.txt", "r")
aaa = {}
for x in asd.readlines():
    x=x.split()
    aaa[x[0]] = float(x[1])
print(aaa)
from collection import normalise
normalise("ĄŚŻŹ")
'''

from vigenere_tester import random_text
from fitting import fitter
from caesar import Caesar
asd = random_text(1000)
print(fitter(asd))
a = Caesar(20)
print(fitter(a.cipher(asd)))

