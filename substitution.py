alphabet_EN=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_PL=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z']

# creator of
def sym_subst_creator(key):
    result={}
    for x in range(len(key)//2):
        #result[template.index(key[x*2])], result[template.index(key[x*2+1])] = key[2*x+1], key[2*x]
        result[key[x*2]], result[key[x*2+1]] = key[x*2+1], key[x*2]
    str.maketrans(result)
    return result


def full_subst_creator(key, template):
    assert len(key)==len(template)
    result={}
    for x,y in zip(key,template):
        result[y]=x
    

a=sym_subst_creator("GADERYPOLUKI")
b="A"
c=str.maketrans(a)
d="ASDZXCASFBDSGFWEHGWERFEFf"
print(d.translate(c))
