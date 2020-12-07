n=int(input("enter number of matrices "))
r=int(input("enter number of rows "))
c=int(input("enter number of columns "))
z=[]
h=[]
for l in range(0,n):
    for k in range(0,r):
        print("enter row",k+1,"of matrix",l+1,"(within [])"end="")
        u=input()
        a=[]
        y=u[1:len(u)-1:1]
        for p in y.split(","):
            a.append(p)   
        h.append(a)
for w in range(0,r):
    del z[:]
    for i in range(0,r):
        z.append(0)
    for o in range(0,n):
        g=h[w+o*r]
        for s in range(0,c):
            t=g[s]
            z[s]=z[s]+int(t)
    print(z)
            
    
