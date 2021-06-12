import requests
import BinanceAPI
import GetPriceSpread


def getQuoteDelta(response):
    output_dict = [x for x in response if x['symbol'].endswith('USDT')]
    sorted_response = BinanceAPI.getJsonSorted(output_dict, 'count')
    #printResult(sorted_response, 'count')
    GetPriceSpread.getPriceSpread(sorted_response)
