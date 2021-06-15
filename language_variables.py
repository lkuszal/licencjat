"""all language dependent variables"""
# Written by Lukasz Cholodecki as part of 2021 thesis
from json import load
from os import path
freq_model = load(open(path.join(path.dirname(__file__), "freq_model.json"), "r"))
thresholds_full = load(open(path.join(path.dirname(__file__), "threshold_full.json"), "r"))
letter_freq = load(open(path.join(path.dirname(__file__), "letter_freq.json"), "r"))
model_kappa = 0.05924
alphabet_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
thresholds_suppressed = {
    100: [0.023711712548595852, 0.015380634944193061, 0.02003437686868687],
    200: [0.017788349431934733, 0.011377657060312733, 0.014325110289855073],
    300: [0.015307891095703395, 0.009543781289099527, 0.011898721674208147],
    400: [0.013693534094066682, 0.008540244010695188, 0.01050851325029656],
    500: [0.012584447989592759, 0.0077749004322047125, 0.009494192415458937],
    750: [0.010926223853846156, 0.00665348067328943, 0.008195588045662101],
    1000: [0.010108817536058377, 0.0059362896532671105, 0.007397472289855072]
}
