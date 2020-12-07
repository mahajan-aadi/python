# it calculates  max size of list with sum of two numbers not
#equal to a certain number

s=list(input().split(","))
k=int(input())

def nonDivisibleSubset(k, s):
    # Write your code here
    m={}
    for i in s:
        m[i]=1
    for i in s:
        for l in s:
            if l==i:
                continue
            else:
                if (l+i)%k==0:
                    m[i]+=1
    if (max(m.values())==1):
        return  len(s)
    else:
        p=list(m.keys())
        q=list(m.values())
        del p[q.index(max(q))]
        return nonDivisibleSubset(k, p)
'''
def nonDivisibleSubset(k, s):
    a=[0]*k
    for i in s:
        a[i%k]+=1
    count=min(a[0],1)
    for i in range(1,k//2+1):
        if i==k-i:
            count+=min(a[i],1)
        else:
            count+=max(a[i],a[-i])
    return count
    '''
