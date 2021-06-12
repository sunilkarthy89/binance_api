import threading
import traceback
from prometheus_client import (
    CollectorRegistry,
    Gauge,
    push_to_gateway
)

def pushdata(symbol, oldSpread, deltap):
    registry = CollectorRegistry()
    #g = Gauge(symbol, oldspread, registry=registry)
    #g = Gauge(symbol, labels = {oldspread}, value = 1623062182.9207761, timestamp = None, registry=registry)
    #print("***Prometheus",symbol, oldSpread, deltap)
    g = Gauge(symbol, 'Spread price', ['Oldspread', 'Delta'], registry=registry).labels(Oldspread=oldSpread, Delta=deltap)
    #g.set_to_current_time()
    push_to_gateway('localhost:8080', job='Binance_data', registry=registry, grouping_key={'Symbol': symbol})
    #push_to_gateway('localhost:9093', job='Binance_data', registry=registry)

