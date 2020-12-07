from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os
s=input("search:")
w=s.replace(" ","_")
if not os.path.isdir(w):
    os.makedirs(w)
para={"q":s}
r=requests.get("https://www.bing.com/images/search",params=para)
soup=BeautifulSoup(r.text,"html.parser")
result=soup.findAll("a",{"class":"thumb"})
for q in result:
    try:
        img_obj=requests.get(q.attrs["href"])
        print("getting:",q.attrs["href"])
        try:
            img=Image.open(BytesIO(img_obj.content))
            title=q.attrs["href"].split("/")[-1]
            img.save("./"+w+"/"+title,img.format)    
        except:
            print("can not save image")
    except:
        print("can not load image")