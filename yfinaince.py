import yfinance as yf
import time
import datetime


def finainces(msg):
    #時間
    localtime= str(datetime.datetime.now())
    HMS= (localtime[11:19])
    StockName = msg[1:]
    up_down=[]
    Change_Rate = 0
    Ticker = yf.Ticker(StockName)
    Tiker2 = Ticker.info['currentPrice']

    Previous_Price = str(Ticker.info['previousClose'])
    Current_Price0 = str(Ticker.info['currentPrice'])
    Current_Price = Current_Price0[:5]
    Price_Gap00 = Ticker.info['currentPrice']-Ticker.info['previousClose']
    Price_Gap0 = str(Price_Gap00)
    Price_Gap = Price_Gap0[:5]
    if Price_Gap00 >0:
        up_down = '漲'
    elif Price_Gap00 <0:
        up_down = '跌'
    Change_Rate00 = (Ticker.info['currentPrice']-Ticker.info['previousClose'])/ Ticker.info['previousClose']*100
    Change_Rate0 = str(Change_Rate00)
    if Change_Rate00 >=0:
        Change_Rate = Change_Rate0[:3]
    elif Change_Rate00 <0:
        Change_Rate = Change_Rate0[:4]
    
    
    final_part=str(f"{HMS} {StockName} 股價:{Previous_Price}, {up_down}{Price_Gap}({Change_Rate}%)")
    
    return final_part
    
    
    #return '為什麼動不了~'
    






