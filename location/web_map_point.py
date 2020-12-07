import json
import requests
import re

key="Arpj03RLMiXFsLUSDfKR8nvzY5g4O0U748nZW1iUCwnzkTqTGGRBYmNhkBmPDJlo"
k=[
 "Address"
, "Neighborhood"
, "PopulatedPlace"
, "Postcode1"
, "AdminDivision1"
, "AdminDivision2"
, "CountryRegion"]
location=input("input coordinates:")
n=1
for m in k:
    print(n,":",m)
    n+=1
sn=int(input())-1
search="http://dev.virtualearth.net/REST/v1/Locations/"+location+"?includeEntityTypes="+k[sn]+"&key="+key
address=requests.get(search)
i=json.loads(address.text)

print("boundries:",i["resourceSets"][0]["resources"][0]["bbox"])
print("\n address:",end="")
print(i["resourceSets"][0]["resources"][0]["address"])