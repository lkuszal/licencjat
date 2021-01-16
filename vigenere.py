alph_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']


def vig_ciph(text, enc_key):
    output = ""
    n = 0
    enc_key = enc_key.lower()
    for line in open(text, "r", encoding="utf8").readlines():
        newline = line.replace("ą", "a").replace("ć", "c").replace("ę", "e").replace("ł", "l").replace(
            "ń","n").replace("ó","o").replace("ś", "s").replace("ż", "z").replace("Ć", "C").replace(
            "Ł", "L").replace("Ó", "O").replace("Ś", "S").replace("Ż", "Z").replace("Ź", "Z").replace("é", "e")
        for ch in newline:
            if ord(ch) in range(97, 123):
                output += chr((ord(enc_key[n % len(enc_key)]) - 97 + ord(ch) - 97) % len(alph_en) + 97)
                n += 1
            elif ord(ch) in range(65, 90):
                output += chr((ord(enc_key[n % len(enc_key)]) - 97 + ord(ch) - 65) % len(alph_en) + 65)
                n += 1
            else:
                output += ch
    return output


if __name__ == "__main__":
    print(vig_ciph("test.txt", "key"))
