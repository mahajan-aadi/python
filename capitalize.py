while(1):
        a=[x for x in input().split(" ")]
        o=""
        for i in a:
            l=ord(i[0])
            l=int(l)-32
            l=chr(int(l))
            p=l+i[1::]
            o=o+p+" "
        print(o)
