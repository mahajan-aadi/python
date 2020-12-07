a=input()
b=[x for x in a.split(" ")]
c=[]
d=[]
e=[]
for i in range(0,int(b[1])):
    l=input()
    q=[x for x in l.split(" ")]
    c.append(int(q[0]))
    d.append(int(q[1]))
e=zip(c,d)
e=list(e)
e.sort(key = lambda x: x[0]) 
(c,d)=zip(*e)
z=int(b[0])
o=0
for l in range(0,int(b[1])):
    t=z-int(c[l])
    if(t<0):
        print("NO")
        o=o+1
        break
    else:
        z=z+int(d[l])
if(o<=0):
    print("YES")
