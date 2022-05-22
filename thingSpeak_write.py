import urllib.request

f1=str(input('Enter the data to feed in field 1 of your channel: '))

WRITE_KEY='https://api.thingspeak.com/update?
api_key=OMWEWOUIY16OQWHF&field1='
b=urllib.request.urlopen(WRITE_KEY+f1)