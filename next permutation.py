# It identifies the next permutation in a sorted list of permutations

def start():
    w=input("enter:")
    j=list(w)
    for i in range(len(j)-1,0,-1):
        if j[i]<=j[i-1]:
            continue
        else:
            break
    if (len(w)==1) or(i==1 and w[0]>=w[1]):
        return "no answer"
    else:
        m="z"
        for l in j[i::]:
            if l<m and l>j[i-1]:
                m=l
        for k in range(len(j)-1,0,-1):
            if j[k]==m:
                j[k],j[i-1]=j[i-1],j[k]
                break;
        a=j[:i:]
        b=j[i::]
        u=a+b[::-1]
        return "".join(u)

a=start()
print(a)
