# description of cipher

# method ensuring that given key is in correct format
def correct(enc_key):
    pass


# method for cipher
def cipher(text, enc_key=None):
    if not correct(enc_key):
        return False


# method for decipher, for selfreversing cipher call cipher function
def decipher(text, enc_key=None):
    if not correct(enc_key):
        return False


# testing
if __name__ == "__main__":
    pass
