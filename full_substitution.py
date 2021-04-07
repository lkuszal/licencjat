# substitution cipher for key's symbols of different length than 1


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


library = {"Morse code": ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                          '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'],
           "multitap": ['2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7',
                        '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999'],
           "A1Z26": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                     '18', '19', '20', '21', '22', '23', '24', '25', '26']}


# testing
if __name__ == "__main__":
    pass
