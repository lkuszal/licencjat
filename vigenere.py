alph_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
def unpol(text):
    output = ""
    for line in open(text,"r", encoding="utf8").readlines():
        newline=replace("ą","a").replace("ć","c").replace("ę","e").replace("ł","l").replace("ń","n").replace("ó","o").replace("ś","s").replace("ż","z")
        for ch in newline:
            if ord(ch) in range(97,123):
                output+=ch
    return output