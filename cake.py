import sys
def a(N):
    for r in range(0,N):
        for i in range(0,N-r):
            print("*",end="")
        for j in range(0,2*r+1):
            print(" ",end="")
        for g in range(0,N-r):
            print("*",end="")
        print()
def b(N):
    for r in range(1,N):
        for i in range(0,r+1):
            print("*",end="")
        for j in range(0,2*(N-r)-1):
            print(" ",end="")
        for g in range(0,r+1):
            print("*",end="")
        print()
try:
    N=eval(sys.argv[1])
except:
    N=int(input("enter "))
if(0<=N<=50):
    if((N==0)or(N==1)or(type(N)!=int)):
        print("impossible")
    else:
        a(N)
        b(N)
