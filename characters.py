name=input('enter ')
##def char(h):
##    c=0
##    for i in name:
##        if(i==h):
##            c=c+1
##    print(h,"=",c)
##l=0
##while l<255:
##    a=chr(l)
##    if(a in name):
##        char(a)
##    l=l+1
import collections
e=collections.Counter(name)
print(e)          
