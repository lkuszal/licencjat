from fitting import fitter
from collection import random_text, suppress


def confidence(length=100, sample_size=10000, alpha=0.98):
    """counts empirically confidence intervals of fitting values, returns thresholds and prints out how many text
    completes all thresholds"""
    asd = [fitter(suppress(random_text(length))) for x in range(sample_size)]
    thresholds = []
    for x in range(len(asd[0])):
        thresholds.append(sorted([asd[y][x] for y in range(len(asd))])[int(sample_size*alpha)-1])
    a = sample_size
    for x in asd:
        for y, z in enumerate(thresholds):
            if x[y] > z:
                a -= 1
                break
    print(a/sample_size)
    return thresholds


print({x:confidence(x) for x in [100,200,300,400,500,750,1000]})

