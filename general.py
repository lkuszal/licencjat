from unidecode import unidecode


# class for keeping plaintext and perform basic operations before ciphering
class Text:
    # initializing object by passing string
    def __init__(self, text):
        assert type(text) is str
        self.plaintext = str(text)
        self.is_supressed = False
        self.is_normalised = True

    # decorator to string conversion
    def __str__(self):
        return self.plaintext
    
    def __iter__(self):
        # from collections.abc import Iterable, Iterator
        return str.__iter__(str(self))

    def upper(self):
        return str.upper(self.plaintext)

    # transforming language specific letters to latin alphabet
    def normalise(self):
        self.plaintext = unidecode(self.plaintext)
        self.is_normalised = True

    # Formating text to clean string containing only latin uppercase letters and numbers
    def suppress(self):
        if self.is_normalised:
            temp_text = ""
            for char in self.plaintext.upper():
                a = ord(char)
                if 64 < a < 91:
                    temp_text += char
            self.plaintext = temp_text
        self.is_supressed = True


# tests
if __name__ == "__main__":
    asd = Text("Chroń pułk twój i sześć flag")
    print(asd)
    asd.normalise()
    print(asd)
    asd.suppress()
    print(asd)
