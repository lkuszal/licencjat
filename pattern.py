import abc


# Describes every cipher class, by default all cipher modules should be based upon this abc class
class MasterCipher(abc.ABC):

    # method of creation key-specific object for given cipher class, if cipher is keyless, return
    # None as attribute key_object
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
