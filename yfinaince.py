import yfinance as yf

def Price( StockName ) :
    Ticker = yf.Ticker(StockName)
    return Ticker.info['currentPrice']