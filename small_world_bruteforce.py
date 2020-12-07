import itertools

E=[{"a","b"},{"a","f"},{"a","c"},{"a","d"},{"a","f"},{"a","j"},{"a","k"},{"a","l"},
   {"b","c"},{"c","e"},{"d","c"},{"d","e"},{"f","e"},{"f","g"},{"g","h"},{"g","i"},
   {"h","k"},{"h","j"},{"h","i"},{"i","j"},{"j","k"},{"k","l"},]
V=["a","b","c","d","e","f","g","j","k","i","l","h","z"]
i="i"
j="z"

def per():
    for n in range(1,len(V)+1):
        a=list(itertools.combinations(V,n))
        a=filter(lambda x:i in x and j in x,a)
        for m in a:
            b=list(itertools.permutations(m))
            b=filter(lambda x:x[0]==i and x[-1]==j,b)
            for t in b:
                istrue=True
                for l in range(len(t)-1):
                    if {t[l],t[l+1]} not in E:
                        istrue=False
                if istrue:
                    return (n-1)
    return("inf")
def cer():
    v=[i for i in V]
    v.remove(i)
    v.remove(j)
    for n in range(len(v)+1):
        a=list(itertools.combinations(v,n))
        for m in a:
            b=list(itertools.permutations(m))
            for t in b:
                t=list(t)
                t.insert(0,i)
                t.append(j)
                istrue=True
                for l in range(len(t)-1):
                    if {t[l],t[l+1]} not in E:
                        istrue=False
                if istrue:
                    return (n+1)
    return("inf")
print(cer())
                
