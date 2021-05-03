import abc


# Contains abstract base class for moddeling ciher classes, which are then used to initialize key-specific objects,
# offering methods to cipher and decipher passed text
# except of  child class, all modules should contain library dictionary contating some of most popular keys (with already
# specified options, or be empty, and unit test
# Describes every cipher class, by default all cipher modules should be based upon this abc class
class MasterCipher(abc.ABC):
    # method of creation key-specific object for given cipher class
    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        self.cipher_key = None
        self.decipher_key = None

    # method for ciphering inputed text, by default using simple str method translate
    @abc.abstractmethod
    def cipher(self, plain_text):
        return plain_text.translate(self.cipher_key)

    # method for deciphering
    @abc.abstractmethod
    def decipher(self, ciphered_text):
        return ciphered_text.translate(self.decipher_key)


# dictionary of some popular keys, ready to use with all needed options (value packed as list)
library = {}

if __name__ == "__main__":
    pass
