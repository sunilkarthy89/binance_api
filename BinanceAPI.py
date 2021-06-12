import json
import requests
import GetPriceSpread
import GetNotionalValue

def getQuoteBTC(response):
    print("***************QUOTE ASSET BTC****************")
    output_dict = [x for x in response if x['symbol'].endswith('BTC')]
    #NumconvJson = [dict([k, v if str(v).isalnum() else float(v) if v else None] for k, v in d.items()) for d in output_dict]
    #output_dict = [x for x in NumconvJson if x['symbol'].endswith('BTC')]
    sorted_response = getJsonSorted(output_dict,'volume')
    #printFullResult(sorted_response, 'volume')
    printResult(sorted_response,'volume')
    getNotValBids(sorted_response)

def getQuoteUSD(response):
    print("***************QUOTE ASSET USDT****************")
    output_dict = [x for x in response if x['symbol'].endswith('USDT')]
    sorted_response = getJsonSorted(output_dict, 'count')
    printResult(sorted_response, 'count')
    #GetPriceSpread.getPriceSpread(sorted_response)

def getNotValBids(sorted_response):
    print("**********TOTAL NOTIONAL VALUE OF TOP 200 BIDS AND ASKS**********")
    print("SYMBOL,BIDS NV,ASKS NV  ")
    #resultJson = sorted_response[0:15]
    resultJson = sorted_response[0:5]
    for i in resultJson:
        bidsnv, asksnv = GetNotionalValue.getNotionalForSymbol(i['symbol'])
        print(i['symbol'], ",", bidsnv, ",", asksnv)

def getJsonSorted(input_dict,sortkey):
    #print("Sorting with Key", sortkey)
    NumconvJson = [dict([k, v if str(v).isalnum() else float(v) if v else None] for k, v in d.items()) for d in input_dict]
    return sorted(NumconvJson, key=lambda vol:vol[sortkey], reverse=True)

def getQuoteDelta(response):
    output_dict = [x for x in response if x['symbol'].endswith('USDT')]
    sorted_response = getJsonSorted(output_dict, 'count')
    #printResult(sorted_response, 'count')
    GetPriceSpread.getPriceSpread(sorted_response)

def getQuoteDeltaTimed(response):
    output_dict = [x for x in response if x['symbol'].endswith('USDT')]
    sorted_response = getJsonSorted(output_dict, 'count')
    # printResult(sorted_response, 'count')
    GetPriceSpread.getPriceSpreadDelta(sorted_response)

def printJson(response):
    print((json.dumps(response, indent=4)))

def printResult(sorted_response, filter):
    resultJson = sorted_response[0:5]
    for i in resultJson:
        print(i.get('symbol'), " : ", i.get(filter))

def printFullResult(sorted_response, filter):
    for i in sorted_response:
        print(i.get('symbol'), " : ", i.get(filter))

if __name__ == '__main__':
    response = (requests.get("https://api.binance.com/api/v3/ticker/24hr")).json()
    #sr = max(response, key=operator.itemgetter(1))[5]
    #print(sr)
    getQuoteBTC(response)   ##Question 1, 3
    getQuoteUSD(response)   ##Question 2
    getQuoteDelta(response) ##Question 4 
    getQuoteDeltaTimed(response)  ##Question 5
    ##Attached screenshot for the prometheus metrics.