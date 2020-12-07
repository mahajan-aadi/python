'''Q- find free time in calenders of two people with given a and b shedule, c1
and c2 contains starting and ending time for meeting to be held and d is
duration of meeting'''
import math
a=[["9:00","10:30"],["12:00","13:00"],["16:00","18:00"]]
c1=["9:00","20:00"]
b=[["10:00","11:30"],["12:30","14:30"],["14:30","15:00"],["16:00","17:00"]]
c2=["10:00","18:30"]
d=30
#o=[["11:30","12:00"]["15:00","16:00"]["18:00","18:30"]]

def time_to_min(given_list):
    output=[]
    for i in given_list:
        a,b=i.split(":")
        c=a+"+"+b+"/60"
        output.append(eval(c))
    return output
def iterate(given):
    output=[]
    for i in given:
        output.append(time_to_min(i))
    return output
def min_to_time(given_list):
    output=[]
    for i in given_list:
        a=math.floor(i)
        b=int((i-a)*60)
        c=str(a)+":"+str(b)
        if(b==0):c+="0"
        output.append(c)
    return output

an,bn=iterate(a),iterate(b)
c1n,c2n=time_to_min(c1),time_to_min(c2)
dn=d/60

big=sorted(an+bn,key=lambda x:(x[0],x[1]))

output=[]
q=0
for i in range(len(big)-1):
    if(big[i][0]<=big[i+1][0]<=big[i][1]):
        continue;
    if(big[i][0]<=big[i+1][0] and big[i+1][0]>=big[i][1] and
       (big[i+1][0]-big[i][1])>=dn ):
        output.append([big[i][1],big[i+1][0]])

p=max(c1n[0],c2n[0])
q=min(c1n[1],c2n[1])
p1=min([i[0] for i in big])
q1=max([i[1] for i in big])

if p<p1:
    output.append([p,p1])
if q1<q:
    output.append([q1,q])

final=[min_to_time(i) for i in output]
print(final)
    
    

        
