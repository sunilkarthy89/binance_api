import json
import requests

def getNotionalForSymbol(symbol):
    #print(symbol)
    url = "https://api.binance.com/api/v3/depth?symbol={0}".format(symbol)
    #print(url)
    json_parse = (requests.get(url)).json()
    bidsnv = getSum(json_parse, 'bids')
    asksnv = getSum(json_parse, 'asks')
    #print(bidsnv, asksnv)
    return bidsnv, asksnv;

def getSum(response, filter):
    #print(response)
    a = []
    for i in (response[filter]):
        metprice = float(i[0])
        metquantity = float(i[1])
        # print(metprice * metquantity)
        a.append(metprice * metquantity)
        # print(i)
    sortedmetnv = sorted(a, reverse=True)
    a.clear()
    # print(sortedbidnv[:200])
    #print("Sum of elements in given list is :", sum(sortedmetnv))
    return sum(sortedmetnv[:200])
