import requests
import json
import re

#itunes
q=["artistName","trackName","CollectionName","genres"]
entities=["movie", "podcast", "music", "musicVideo", "audiobook", "shortFilm", "tvShow", "software", "ebook"]
query=input("search=")
query=re.sub(" ","+",query)
number=int(input("enter number of terms="))
for i in range(1,len(entities)+1):
    print(i,":",entities[i-1])
se=int(input("media="))
ty=entities[se-1]

w=[]
if(se==2 or se==1 or se==6):
    w.extend([q[0],q[1]])
elif(se==4 or se==3 or se==7):
    w.extend([q[0],q[1],q[2]])
elif(se==5):
    w.extend([q[0],q[2]])
elif(se==8):
    w.append(q[1])
elif(se==9):
    w.extend([q[0],q[1],q[3]])

if(se==3 or se==7):   
    para={"term":query,"&media":ty}
elif(se==6):
    para={"term":query,"entity":"movie","attribute":"shortFilmTerm"}
else:
    para={"term":query,"entity":ty}
para["limit"]=number
search=requests.get("https://itunes.apple.com/search?",params=para)
py=json.loads(search.text)
p=1
for i in py['results']:
    print(p,":")
    for n in range(len(w)):
        try:
            print(w[n],":",i[w[n]])
        except:
            pass
    p=p+1
