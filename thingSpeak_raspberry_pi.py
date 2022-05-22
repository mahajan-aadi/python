import sys
import os
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT
import urllib.request as req

dhtpin = 21
key = "OMWEWOUIY16OQWHF"


def getSensorData():
    RH, T = Adafruit_DHT.read_retry
    (Adafruit_DHT.DHT11, dhtpin)
    return (str(RH), str(T))


def main():
    print('starting...')
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key
    while True:
        try:
            RH, T = getSensorData()
            f = req.urlopen
            (baseURL + "&field1=%s&field2=%s" % (RH, T))
            print("Url: %s" % baseURL)
            print("temp: %s C" % T + ' ' + "Humid: %s %%" % RH)
            f.close()
            sleep(5)
        except:
            print('exiting..')
            break


if __name__ == "__main__": main()
main() 