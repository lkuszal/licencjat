def simplify(text):
    output = ""
    for line in open(text,"r", encoding="utf8").readlines():
        newline=line.casefold().replace("ą","a").replace("ć","c").replace("ę","e").replace("ł","l").replace("ń","n").replace("ó","o").replace("ś","s").replace("ż","z")
        for ch in newline:
            if ord(ch) in range(97,123):
                output+=ch
    return output

def counting(text,length):
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w','x', 'y', 'z']
    freq={}
    for x in range(length):
        freq[x]={}
        for y in letters:
            freq[x][y]=0
    index=0
    for ch in text:
        freq[index%length][ch]+=1
        index+=1
    return freq
if __name__=="__main__":
    print(counting(simplify("C:/pt.txt"),5))
