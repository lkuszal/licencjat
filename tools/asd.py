from general import Text
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
    corpus = Text(source_text.read())
    corpus.normalise()
    corpus.suppress()
    for x in range(1,2):
        pass
        dict_scrapper(freq.frequencies(corpus, x))
        # print(freq.poli_frequencies(corpus, 10))
        # dict_scrapper(freq.words_edges_frequencies(corpus, x, beginning=False))
        # dict_scrapper(freq.short_words_frequencies(corpus, x))
    # print(freq.kappa_count(freq.frequencies(corpus)))


