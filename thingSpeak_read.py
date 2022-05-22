import urllib.request
import json
url="https://api.thingspeak.com/channels/1662172
/fields/2.json?results=10"
def main():
    a = urllib.request.urlopen(url)
    response = a.read().decode()
    print("http status code=",a.getcode())
    data=json.loads(response)
    for i in data['feeds'] :
        print ("Field data =",i['field2'])
        print("It was created at:",i['created_at'])
        print("\n")
    a.close()
main()