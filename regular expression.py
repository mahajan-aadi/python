import re
a=re.compile(r'([\d]{3})[-]([\d]{3})[-]([\d]{4})')
l=(open("q.txt",'r')).read()
if(a.finditer(l)):
    print("h")
else:
    print("r")
