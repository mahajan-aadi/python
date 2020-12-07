a=input("enter")
p=[]
for x in a.split(","):
    p.append(x)
value=[]
for d in p:
    value.append(str(round((2*50/30*int(d))**0.5)))
print(",".join(value))

##a=input("enter")
##p=[x for x in a.split(',')]
##value=[]
##for d in p:
##    value.append(str(round((2*50/30*int(d))**0.5)))
##print(",".join(value))

##import math
##c=50
##h=30
##value = []
##items=[x for x in input().split(',')]
##for d in items:
##    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
##
##print (','.join(value))
