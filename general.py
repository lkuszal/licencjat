from unidecode import unidecode


# class for keeping plaintext and perform basic operations before ciphering
class Text:
    # initializing object by passing string
    def __init__(self, text):
        assert type(text) is str
        self.plaintext = text
        self.normalised_plaintext = None
        self.suppressed_plaintext = None

    # class to string conversion
    def __str__(self):
        if self.suppressed_plaintext:
            return self.suppressed_plaintext
        elif self.normalised_plaintext:
            return self.normalised_plaintext
        else:
            return self.plaintext
    
    def __iter__(self):
        # from collections.abc import Iterable, Iterator
        return str.__iter__(str(self))

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


# tests
if __name__ == "__main__":
    '''
    asd = Text("Chroń pułk twój i sześć flag")
    print(asd)
    asd.normalise()
    print(asd)
    asd.suppress()
    print(asd)
    abc = Text(a)
    abc.normalise()
    abc.suppress()
    '''
    # performance tests
    a = open("pt.txt", "r", encoding="utf8").read()
    import time, mono_substitution, caesar, rev_substitution
    a = open("pt.txt", "r", encoding="utf8").read()
    b=Text(a)
    c=Text(a)
    d=Text(a)
    b.normalise(), b.suppress()
    c.normalise(), b.suppress()
    d.normalise(), d.suppress()
    a1=time.perf_counter()
    caesar.cipher(str(b),"13")
    a2=time.perf_counter()
    b1=time.perf_counter()
    mono_substitution.cipher(str(c),"NOPQRTUVWXYZABCDEFGHIJKLM")
    b2=time.perf_counter()
    c1=time.perf_counter()
    rev_substitution.cipher(str(d), "ANBOCPDQERFSGTHUIVJWKXLYMZ")
    c2=time.perf_counter()
    print(a2-a1,b2-b1, c2-c1)
