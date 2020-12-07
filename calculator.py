run=0
previous="0+"
import re
while run==0:
    if previous=="0+":
        print("enter equation ",end="")
    eq=input()
    if (eq == "exit") or (eq == "quit"):
        print("bye")
        run=1
    elif eq == "ac":
        eq="0+"
        previous="0+"
    else:
        eq=re.sub('[A-Za-z"",[]{}:]','',eq)
        eq=str(previous)+str(eq)
        eq=eval(eq)
        previous=eq
        print(eq,end="")
