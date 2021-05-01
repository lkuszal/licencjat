from abc import ABCMeta


# Describes every cipher class, by default all cipher modules should be based upon this abc class
class MasterCipher(metaclass=ABCMeta):

    # method of creation key-specific object for given cipher class, if cipher is keyless, return
    # None as attribute key_object
    def __init__(self, key, **kwargs):
        return self.key_object

    # method for ciphering inputed text
    def cipher(self, plain_text):
        return self, ciphered_text

    # method for deciphering
    def decipher(self, ciphered_text):
        return self, plain_text

