# bunch of frequently used objects to import into another modules
from random import choices
alph_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PL_freq = [0.10011, 0.015, 0.04437, 0.03292, 0.09095, 0.00293, 0.01365, 0.0107, 0.08368, 0.02367, 0.03399, 0.03984,
           0.02963, 0.05671, 0.08448, 0.03078, 2e-05, 0.04497, 0.04946, 0.03937, 0.02296, 0.00027, 0.04507, 0.00018,
           0.03836, 0.06591]


def word_generator(length):
    return "".join(choices(alph_EN,k=length))
