import abc


# Describes every cipher class, by default all cipher modules should be based upon this abc class
class MasterCipher(abc.ABC):

    # method of creation key-specific object for given cipher class, if cipher is keyless, return
    # None as attribute key_object
    @abc.abstractmethod
    def __init__(self):
        self.__cipher_key = None
        self.__decipher_key = None

    # method for ciphering inputed text
    @abc.abstractmethod
    def cipher(self, plain_text):
        return self, ciphered_text

    # method for deciphering
    @abc.abstractmethod
    def decipher(self, ciphered_text):
        return self, plain_text
