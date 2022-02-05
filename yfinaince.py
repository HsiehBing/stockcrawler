import yfinance as yf
import time
import datetime
import pickle


def finainces(msg):
    if msg[1].isalpha()==False :
#    if msg[1]  not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        a_file = open("Input.pkl", 'rb')
        Input = pickle.load(a_file)
        a_file.close()
        msg = Input[msg[1:]]
        localtime= str((datetime.datetime.now()) + datetime.timedelta(hours = 8))
        HMS= (localtime[11:19]) 
        StockName = msg
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
        a_file = open("Output.pkl", 'rb')
        Output = pickle.load(a_file)
        a_file.close()
        StockNameE = Output[StockName]
        
        
        final_part=str(f"{HMS} {StockNameE} 股價:{Current_Price0}, {up_down}{Price_Gap}({Change_Rate}%)")
        
        return final_part



    else:
    #時間
        localtime= str((datetime.datetime.now()) + datetime.timedelta(hours = 8))
        HMS= (localtime[11:19]) 
        StockName = msg[1:].lower()
        StockNameE = msg[1:].upper()
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
        
        
        final_part=str(f"{HMS} {StockNameE} 股價:{Current_Price0}, {up_down}{Price_Gap}({Change_Rate}%)")
        
        return final_part
    
    
    #return '為什麼動不了~'
    






