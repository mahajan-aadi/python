while(2>0):
    x=int(input("enter rows "))
    y=0
    while(y<=x):
        k=0   
        z=x-y
        q=0
        while((2*z+y)>=q):
            print(" ",end="")
            q=q+1
        while(k<=y):
            a=1
            p1=1
            while(a<=y):
                p1=a*p1
                a=a+1
            b=1
            p2=1
            while(b<=k):
                p2=b*p2
                b=b+1
            z=y-k
            p3=1
            c=1
            while(c<=z):
                p3=c*p3
                c=c+1
            w=p1/(p2*p3)
            print(format(w,".0f"),end=" ") 
            k=k+1
        print("")
        y=y+1
    
