def fact(n):
  if n==1:
    return 1
  else:
    return n*fact(n-1)
i=list(x for x in input())
r=0
for l in range(fact(len(i))):
  if(r>len(i)-1):
    r=r%len(i)
  i[r-1],i[r]=i[r],i[r-1]
  print("".join(i))
  r+=1
