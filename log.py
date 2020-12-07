import re
import sys
p=sys.argv[1]
b=sys.argv[2]
p=p+b
search=r'(?i)ERROR'
with open(p,'r') as a:
    for line in a:
        o=re.search(search,line)
        if o is None:
            continue
        else:
            print(line)
