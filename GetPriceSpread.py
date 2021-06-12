import BinanceAPI
import json
import requests
import Prometheusgateway
from time import time, sleep
import re

def getPriceSpread(sorted_response):
    resultJson = sorted_response[0:5]
    print("***************PRICE SPREAD****************")
    for i in resultJson:
        spread = float(i.get('askPrice') - i.get('bidPrice'))
        print(i.get('symbol'), " : ", spread)

class DeltaaDictionary(dict):
    # __init__ function
    def __init__(self):
        self = dict()

    # Function to check and add key:value
    def add(self, key, value):
        self[key] = value
        # if self.__contains__(key):
        #     self.update(key = value)
        # else:
        #     self[key] = value

    #def find(self,key):

deltaa = DeltaaDictionary()

def getPriceSpreadDelta(sorted_response):
    resultJson = sorted_response[0:5]
    for i in resultJson:
        tsymbol = i.get('symbol')
        spread = delta = float(i.get('askPrice') - i.get('bidPrice'))
        print(tsymbol, spread, spread)
        #temp = {"\"symbol\": \"{}\", \"spread\":{}".format(tsymbol, spread)}
        #goodt = (str(temp).replace("'", "")).replace('"',"'")
        deltaa.add(tsymbol, spread)
    ##Looping the funtion looperData for every 10 seconds
    #threading.Timer(10.0, looperDelta(deltaa)).start()
    while True:
        sleep(5)
        #print(deltaa)
        looperDelta(deltaa)

def looperDelta(dict):
     for tsymbol in list(dict):
        #print(tsymbol)
        newSpread = getNewSpread(tsymbol)
        oldspread = dict.get(tsymbol)
        #print("old spread :", oldspread)
        #print("new Spread :", newSpread)
        delta = oldspread - newSpread
        print(tsymbol, newSpread, delta)
        Prometheusgateway.pushdata(tsymbol, newSpread, delta)
        deltaa.add(tsymbol, newSpread)

def getNewSpread(symbol):
    #jslist = json.dumps(odlist)
    #print(symbol)
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol={0}".format(symbol)
    json_parse = (requests.get(url)).json()
    #print("*****",float(json_parse['askPrice']) - float(json_parse['bidPrice']))
    return float(json_parse['askPrice']) - float(json_parse['bidPrice'])
