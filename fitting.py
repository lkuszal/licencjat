"""functions connected with checking goodness of fit of text to model values"""
import freq
import ciphpy.collection as collection
model = collection.freq_model


def fitter(text, max_length=3):
    """function getting all possible statistic about goodness of fit of text comparing to model. If text doesn't
    contain any spaces, function will only check for characters frequencies, otherwise will also run for word edges and
    short words. Calls rating function, so depending on algorithm of that will return different values. Returns
    first-level list"""
    text = collection.normalise(text)
    let_frq = []
    for x in range(1, max_length+1):
        let_frq.append(freq.frequencies(collection.suppress(text), x))
    all_frq = [let_frq]
    if " " in text:
        beg_frq = []
        end_frq = []
        wrd_frq = []
        for x in range(1, max_length+1):
            beg_frq.append(freq.words_edges_frequencies(text, x, beginning=True))
            end_frq.append(freq.words_edges_frequencies(text, x, beginning=False))
            wrd_frq.append(freq.short_words_frequencies(text, x))
        all_frq.extend([beg_frq, end_frq, wrd_frq])
    return [rating(all_frq[x][y], model[x][y]) for x in range(len(all_frq)) for y in range(max_length)]


def rating(obs, exp):
    """function that returns value representing goodness of fit between observated values (as dictionary, containing
    counted occurences) and expected values given as dictionary of frequencies"""
    diff = 0
    n = sum(obs.values())
    for x in exp.keys():
        if x in obs.keys():
            diff += abs(exp[x] - obs[x]/n)
        else:
            diff += exp[x]
    return diff/len(exp.keys())


def lang_checker(text):
    """compares given text to language model tresholds, returning sum of differences if checked one is over threshold
    (presented as relative of threshold value)"""
    scores = fitter(text)
    diff = 0
    if len(scores) == 3:
        n = min([[abs(250 - a), a] for a in collection.thresholds_suppressed.keys()])[1]
        for x, y in zip(scores, collection.thresholds_suppressed[str(n)]):
            if x > y:
                diff += x/y
    else:
        n = min([[abs(250 - int(a)), int(a)] for a in collection.thresholds_full.keys()])[1]
        for x, y in zip(scores, collection.thresholds_full[str(n)]):
            print(x,y)
            if x > y:
                diff += x/y
    return diff
    
    
if __name__ == "__main__":
    print(fitter(open("pt.txt", "r", encoding="utf-8").read()))
