from general import Text
import freq

source_text = open("output_lines.txt", "r", encoding="utf-8")
corpus = Text(source_text.read())
corpus.normalise()
# corpus.suppress()
# print(freq.frequencies(corpus, 4))
# print(freq.poli_frequencies(corpus, 10))
# print(freq.words_edges_frequencies(corpus, 3, beginning=False))
print(freq.short_words_frequencies(corpus, 1))
