import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
number='+91' + "7409121142"
ch_number=phonenumbers.parse(number ,"CH")
print(geocoder.description_for_number(ch_number,"en"))
service_provider=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))