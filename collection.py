"""bunch of frequently used objects to import into another modules"""
from language_variables import alphabet_list
def word_generator(length):
    from random import choices
    return "".join(choices(alphabet_list, k=length))


from unidecode import unidecode
def normalise(text):
    return unidecode(text)


def suppress(text):
    temp_text = ""
    for char in text.upper():
        if char.isalpha():
            temp_text += char
    return temp_text


def random_text(length, file="output_lines.txt", file_length=39568):
    """returns random fragment of given lenght from file"""
    from linecache import getline
    from random import randrange
    a = randrange(file_length - length // 10)
    text = ''
    while len(text) < length:
        text += getline(file, a)
        a += 1
    return text[:length]


if __name__ == "__main__":
    print(normalise(random_text(500)))
