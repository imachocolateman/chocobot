import ccxt

# print(ccxt.exchanges)

binance = ccxt.binance()

btc_ticker = binance.fetch_ticker('BTC/USDT')
print(btc_ticker)