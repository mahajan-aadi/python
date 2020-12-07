V=[{"a","b"},{"a","f"},{"a","c"},{"a","d"},{"a","f"},{"a","j"},{"a","k"},{"a","l"},
   {"b","c"},{"c","e"},{"d","c"},{"d","e"},{"f","e"},{"f","g"},{"g","h"},{"g","i"},
   {"h","k"},{"h","j"},{"h","i"},{"i","j"},{"j","k"},{"k","l"},]
N=["a","b","c","d","e","f","g","j","k","i","l","h","z"]
Q={}
for i in N:
    Q[i]="inf"
M=[]
start="i"
M.append(start)
Q[start]=0
D=0

while len(M)>0:
    y=M[0]
    M.pop(0)
    for i in V:
        if y in i:
            w=[l for l in i if l!=y][0]
            if Q[w]=="inf":
                Q[w]=Q[y]+1
                M.append(w)
print(Q)
