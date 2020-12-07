import json
import requests
import re

key="Arpj03RLMiXFsLUSDfKR8nvzY5g4O0U748nZW1iUCwnzkTqTGGRBYmNhkBmPDJlo"
q=input("search:")
maxResults=int(input("maxResults:"))
para={"query":q,"maxResults":maxResults,"key":key}
search=requests.get("http://dev.virtualearth.net/REST/v1/Locations/",params=para)
js=json.loads(search.text)
n=1
for i in js["resourceSets"][0]["resources"]:
    print(n,":")
    print("boundries:",i["bbox"])
    print("\ncoordinates:",i["point"]["coordinates"])
    print("\naddress:",i["address"])
    n+=1
