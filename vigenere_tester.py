from linecache import getline
from random import randrange
from general import normalise, suppress
from vigenere import Vigenere
from collection import word_generator


def random_text(length, file="tools/output_lines.txt", file_length=39568):
    a = randrange(file_length-length//10)
    text = ''
    while len(text) < length:
        text += getline(file, a)
        a += 1
    return text[:length]


def vigenere_generator(length, key_length):
    key = word_generator(key_length)
    asd = suppress(normalise(random_text(length)))
    lalka = Vigenere(key)
    return lalka.cipher(asd), key


if __name__ == "__main__":
    print(vigenere_generator(151, 4))
    print(len(random_text(151)))
