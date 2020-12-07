import json
import requests
import re

key="Arpj03RLMiXFsLUSDfKR8nvzY5g4O0U748nZW1iUCwnzkTqTGGRBYmNhkBmPDJlo"
inputs=["CountryRegion","adminDistrict","locality","postalCode","addressLine","maxResults","includeNeighborhood"]
print("(input '' if not available)")
para={}

for i in inputs:
    if(i=="includeNeighborhood"):
        print(i,"(yes/no):",end="")
        z=input()
        if(z=="yes"):
            para[i]=1
            continue
        else:
            para[i]=0
            continue
    print(i,":",end="")
    z=input()
    if(z==""):
        continue
    para[i]=re.sub(" ", "+", z)
para["key"]=key
site=requests.get("http://dev.virtualearth.net/REST/v1/Locations/",params=para)
js=json.loads(site.text)
n=1
for i in js["resourceSets"][0]["resources"]:
    print(n,":")
    print("boundries:",i["bbox"])
    print("coordinates:",i["point"]["coordinates"])
    print("address:",end="")
    print(i["address"])
    n+=1
