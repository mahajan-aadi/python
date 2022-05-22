t=int(input("enter "))
y=1
while(y<=t):
    if(y==t):
        print(y,":",y*y)
        y=y+1
    else:
        print(y,":",y*y,end=", ")
        y=y+1
