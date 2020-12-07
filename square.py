a=[i for i in input("enter ").split(",")]
z=[]
for p in a:
    y=str((int(p)*int(p)))
    e=p+":"+y
    z.append(e)
print(", ".join(z))
    
