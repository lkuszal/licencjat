"""bunch of frequently used objects to import into another modules"""
alph_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

PL_freq = [0.10011, 0.015, 0.04437, 0.03292, 0.09095, 0.00293, 0.01365, 0.0107, 0.08368, 0.02367, 0.03399, 0.03984,
           0.02963, 0.05671, 0.08448, 0.03078, 2e-05, 0.04497, 0.04946, 0.03937, 0.02296, 0.00027, 0.04507, 0.00018,
           0.03836, 0.06591]

thresholds_full = {
    100: [0.019275, 1, 1, 0.057512, 1, 1, 0.062059, 1, 1, 1, 1, 1],
    200: [0.015148, 0.010128, 1, 1, 1, 1, 0.0483, 1, 1, 1, 1, 1],
    300: [0.012547299, 0.008375887, 1, 1, 1, 1, 0.040191347, 1, 1, 1, 1, 1],
    400: [0.011086907, 0.00771328, 1, 1, 1, 1, 0.037040258, 1, 1, 1, 1, 1],
    500: [0.01052275, 0.006553827, 0.006703591, 1, 1, 1, 0.032004293, 1, 1, 1, 1, 1],
    750: [0.008719527, 0.005699251, 0.005661236, 1, 0.017699873, 1, 0.028294449, 0.016149334, 1, 1, 1, 1],
    1000: [0.007881, 0.005162, 0.004893, 0.026804, 0.016597, 1, 0.025271403, 0.014771, 0.019404258, 0.120518112, 1, 1]
}
thresholds_suppressed = {
    100: [0.023711712548595852, 0.015380634944193061, 0.02003437686868687],
    200: [0.017788349431934733, 0.011377657060312733, 0.014325110289855073],
    300: [0.015307891095703395, 0.009543781289099527, 0.011898721674208147],
    400: [0.013693534094066682, 0.008540244010695188, 0.01050851325029656],
    500: [0.012584447989592759, 0.0077749004322047125, 0.009494192415458937],
    750: [0.010926223853846156, 0.00665348067328943, 0.008195588045662101],
    1000: [0.010108817536058377, 0.0059362896532671105, 0.007397472289855072]
}


from pickle import load
model = load(open("pl_model.p", "rb"))


from random import choices
def word_generator(length):
    return "".join(choices(alph_EN, k=length))


from unidecode import unidecode
def normalise(text):
    return unidecode(text)


def suppress(text):
    temp_text = ""
    for char in text.upper():
        a = ord(char)
        if 64 < a < 91:
            temp_text += char
    return temp_text


from linecache import getline
from random import randrange
def random_text(length, file="output_lines.txt", file_length=39568):
    """returns random fragment of given lenght from file"""
    a = randrange(file_length - length // 10)
    text = ''
    while len(text) < length:
        text += getline(file, a)
        a += 1
    return text[:length]


if __name__ == "__main__":
    pass
