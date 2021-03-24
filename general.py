from unidecode import unidecode


# class for keeping plaintext and perform basic operations before ciphering
class Text:
    # initializing object by passing string
    def __init__(self, text):
        assert type(text) is str
        self.plaintext = text
        self.normalised_plaintext = None
        self.suppressed_plaintext = None

    # transforming language specific letters to latin alphabet
    def normalise(self):
        self.normalised_plaintext = unidecode(self.plaintext)
    
    # Formating text to clean string containing only latin uppercase letters and numbers
    def suppress(self):
        if self.normalised_plaintext:
            temp_text = ""
            for char in self.normalised_plaintext.upper():
                a = ord(char)
                if 64 < a < 91 or 47 < a < 58:
                    temp_text += char
            self.suppressed_plaintext = temp_text


# counting frequency of character in given text
def frequencies(item):
    freq_dict = {}
    for char in item:
        if char in freq_dict.keys():
            freq_dict[char] += 1
        else:
            freq_dict[char] = 0
    return freq_dict


# tests
if __name__ == "__main__":
    '''
    asd = Text("Chroń pułk twój i sześć flag")
    asd.normalise()
    asd.suppress()
    print(asd.normalised_plaintext)
    print(asd.suppressed_plaintext)
    print(asd.frequencies(asd.suppressed_plaintext))
    a = open("pt.txt", "r", encoding="utf8").read()
    abc = Text(a)
    abc.normalise()
    abc.suppress()
    print(abc.frequencies(abc.suppressed_plaintext))
    '''
    import time, caesar, caesar_trans
    a = open("pt.txt", "r", encoding="utf8").read()
    b=Text(a)
    c=Text(a)
    b.normalise(), b.suppress()
    c.normalise(), b.suppress()
    a1=time.perf_counter()
    caesar.cipher(str(a),"13")
    a2=time.perf_counter()
    b1=time.perf_counter()
    caesar_trans.cipher(str(b),"13")
    b2=time.perf_counter()
    print(a2-a1,b2-b1)
