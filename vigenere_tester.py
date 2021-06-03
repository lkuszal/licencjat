from ciphers.vigenere import Vigenere
from collection import word_generator, normalise, suppress, random_text


def vigenere_generator(length, key_length, supresssion=False):
    """returns text of given length (ciphered by random key of given length) and this key"""
    key = word_generator(key_length)
    text = normalise(random_text(length))
    if supresssion:
        text = suppress(text)
    asd = Vigenere(key)
    return asd.cipher(text), key


if __name__ == "__main__":
    print(vigenere_generator(151, 4))


