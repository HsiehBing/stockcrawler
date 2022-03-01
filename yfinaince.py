#代號#
import yfinance as yf
import time
import datetime
import pickle
import requests
import bs4
from bs4 import BeautifulSoup
Name = ('TSE','大盤', 'OTC', '上櫃', '小台1', '小台2')
TSE_i = ('TSE', '大盤')
OTC_i =('OTC','上櫃')


def finainces(msg):
    Name = msg[1:]
    localtime= str((datetime.datetime.now()) + datetime.timedelta(hours = 8))
    HMS= (localtime[11:19])

    if Name in msg[1:]:
        up_down=[]

        ##上市
        if Name in TSE_i:
            url = 'https://tw.quote.finance.yahoo.net/quote/q?type=tick&perd=1m&mkt=10&sym=%23001&callback=jQuery111301426021457469553_1644243086726&_=1644243086727'
            indexNameE = '上市指數'
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser").text
            sChange_Rate = (soup[soup.find('"185"')+6:soup.find('"443"')-1])
            Current_Point = (soup[soup.find('"125"')+6:soup.find('"126"')-1])
            Change_Point = (soup[soup.find('"184"')+6:soup.find('"185"')-1])
            Point_Gap = round(float(Change_Point),2)
            Change_Rate = round(float(sChange_Rate),2)
            if Point_Gap >0:
                up_down = '漲'
            elif Point_Gap <0:
                up_down = '跌'       
            final_part=str(f"{HMS} {indexNameE} 指數:{Current_Point}, {up_down}{Change_Point} ({Change_Rate}%)")
            return final_part
            

        ##上櫃
        elif Name in OTC_i:
            url = 'https://tw.quote.finance.yahoo.net/quote/q?type=tick&perd=1m&mkt=10&sym=%23026&callback=jQuery1113011660253264229259_1644245704375&_=1644245704376'
            indexNameE = '上櫃指數'
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser").text
            sChange_Rate = (soup[soup.find('"185"')+6:soup.find('"185"')+11])
            Current_Point = (soup[soup.find('"125"')+6:soup.find('"126"')-1])
            Change_Point = (soup[soup.find('"184"')+6:soup.find('"185"')-1])
            Point_Gap = round(float(Change_Point),2)
            Change_Rate = round(float(sChange_Rate),2)
            if Point_Gap >0:
                up_down = '漲'
            elif Point_Gap <0:
                up_down = '跌'       
            final_part=str(f"{HMS} {indexNameE} 指數:{Current_Point}, {up_down}{Change_Point} ({Change_Rate}%)")
            return final_part 

        elif Name == '小台1':
            url = 'https://tw.screener.finance.yahoo.net/future/q?type=tick&perd=1m&mkt=01&sym=WMT%26&callback=jQuery111307042559616830528_1644316771914&_=1644316771915'
            indexNameE = '小台近1'
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser").text
            sChange_Rate = (soup[soup.find('"185"')+6:soup.find('"185"')+11])
            Current_Point = (soup[soup.find('"125"')+6:soup.find('"126"')-1])
            Change_Point = (soup[soup.find('"184"')+6:soup.find('"185"')-1])
            Point_Gap = round(float(Change_Point),2)
            Change_Rate = round(float(sChange_Rate),2)
            if Point_Gap >0:
                up_down = '漲'
            elif Point_Gap <0:
                up_down = '跌'       
            final_part=str(f"{HMS} {indexNameE} 指數:{Current_Point}, {up_down}{Change_Point} ({Change_Rate}%)")
            return final_part 


        elif Name == '小台2':
            url = 'https://tw.screener.finance.yahoo.net/future/q?type=tick&perd=1m&mkt=01&sym=WMT%40&callback=jQuery11130047334692729293915_1644316909549&_=1644316909550'
            indexNameE = '小台近2'
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser").text            
            sChange_Rate = (soup[soup.find('"185"')+6:soup.find('"185"')+11])
            Current_Point = (soup[soup.find('"125"')+6:soup.find('"126"')-1])
            Change_Point = (soup[soup.find('"184"')+6:soup.find('"185"')-1])
            Point_Gap = round(float(Change_Point),2)
            Change_Rate = round(float(sChange_Rate),2)
            if Point_Gap >0:
                up_down = '漲'
            elif Point_Gap <0:
                up_down = '跌'       
            final_part=str(f"{HMS} {indexNameE} 指數:{Current_Point}, {up_down}{Change_Point} ({Change_Rate}%)")
            return final_part


 #########################################################################################################################      
        
    #######    
    if msg[1].encode('UTF-8').isalpha()==False :
        a_file = open("r_Input.pkl", 'rb')
        Input = pickle.load(a_file)
        a_file.close()
        msg = Input[msg[1:]]
        # localtime= str((datetime.datetime.now()) + datetime.timedelta(hours = 8))
        # HMS= (localtime[11:19]) 
        stockName = msg
        up_down=[]

        Change_Rate = 0
        res = requests.get(f'https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;autoRefresh=1642576273209;symbols=[{stockName}];type=tick?bkt=&device=desktop&ecma=modern&feature=ecmaModern,useVersionSwitch,useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=anhj1hpgufeaf&region=TW&site=finance&tz=Asia/Taipei&ver=1.2.1214&returnMeta=true')
        jd = res.json()['data']
        meta =(jd[0]['chart']['meta'])
        Previous_Price =round((meta['previousClose']),2)
        
        Current_Price = round((meta['regularMarketPrice']),2)
        Price_Gap = round((Current_Price-Previous_Price),2)


        if Price_Gap >0:
            up_down = '漲'
        elif Price_Gap <0:
            up_down = '跌'
        Change_Rate = round((Price_Gap/Previous_Price*100),2)
        a_file = open("r_Output.pkl", 'rb')
        Output = pickle.load(a_file)
        a_file.close()
        StockNameE = Output[stockName]
        final_part=str(f"{HMS} {StockNameE} 股價:{Current_Price}, {up_down}{Price_Gap} ({Change_Rate}%)")
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



