"""bunch of frequently used objects to import into another modules"""
alph_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
from os import path

thresholds_suppressed = {
    100: [0.023711712548595852, 0.015380634944193061, 0.02003437686868687],
    200: [0.017788349431934733, 0.011377657060312733, 0.014325110289855073],
    300: [0.015307891095703395, 0.009543781289099527, 0.011898721674208147],
    400: [0.013693534094066682, 0.008540244010695188, 0.01050851325029656],
    500: [0.012584447989592759, 0.0077749004322047125, 0.009494192415458937],
    750: [0.010926223853846156, 0.00665348067328943, 0.008195588045662101],
    1000: [0.010108817536058377, 0.0059362896532671105, 0.007397472289855072]
}


from json import load
freq_model = load(open(path.join(path.dirname(__file__),"freq_model.json"), "r"))
thresholds_full = load(open(path.join(path.dirname(__file__),"threshold_full.json"), "r"))
letter_freq = load(open(path.join(path.dirname(__file__),"letter_freq.json"), "r"))


def word_generator(length):
    from random import choices
    return "".join(choices(alph_EN, k=length))


def normalise(text):
    from unidecode import unidecode
    return unidecode(text)


def suppress(text):
    temp_text = ""
    for char in text.upper():
        a = ord(char)
        if 64 < a < 91:
            temp_text += char
    return temp_text


def random_text(length, file="output_lines.txt", file_length=39568):
    """returns random fragment of given lenght from file"""
    from linecache import getline
    from random import randrange
    a = randrange(file_length - length // 10)
    text = ''
    while len(text) < length:
        text += getline(file, a)
        a += 1
    return text[:length]


if __name__ == "__main__":
    pass
