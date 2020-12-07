import json
import requests
import re

key="Arpj03RLMiXFsLUSDfKR8nvzY5g4O0U748nZW1iUCwnzkTqTGGRBYmNhkBmPDJlo"
methods=["EatDrink","SeeDo","Shop,BanksAndCreditUnions","Hospitals","HotelsAndMotels","Parking"]
main=["businessAndPOI","naturalPOI","address"]
sain=["businessesAtLocation","naturalPOIAtLocation","addressOfLocation"]
para={}
point=input("enter cootdinates:")
para["radius"]=input("enter radius(Km):")
n=1
for i in main:
    print(n,":",i)
    n+=1
se=int(input())
para["includeEntityTypes"]=main[se-1]
n=1
if se==1:
    for i in methods:
        print(n,":",i)
        n+=1
    po=int(input())
    para["type"]=methods[po-1]
para["key"]=key
para["verboseplacenames"]="true"

search="https://dev.virtualearth.net/REST/v1/LocationRecog/"+point+"?"
res=requests.get(search,params=para)
js=json.loads(res.text)
if se==1:
    for i in (js["resourceSets"][0]["resources"][0][sain[se-1]]):
        print(i["businessAddress"]["formattedAddress"])
        print([i["businessInfo"]])
else:
    print(js["resourceSets"][0]["resources"][0][sain[se-1]])