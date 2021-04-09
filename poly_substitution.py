# substitution cipher where every letter is replaced by some string (usually choosen by random from few options),
# but every string is unique between letter's collections


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


# dictionary containing frequently used keys, or empty one, in case of passing additional argument to function,
# whole value should be collected as a tuple
library = {"name": "enc_key"}

# testing
if __name__ == "__main__":
    pass
