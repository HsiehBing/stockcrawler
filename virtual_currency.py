##開頭V
import requests
import bs4
from bs4 import BeautifulSoup
import datetime

def Vitual_Currency(msg):

    vsName = msg[1:].upper()
    res = requests.get(f'https://api.binance.com/api/v1/ticker/24hr?symbol={vsName}USDT')
    jd = res.json()

    #price
    currentPrice =float(jd['lastPrice']) 
    #name
    name = jd['symbol'].replace("USDT", '')
    different =float(jd['priceChange']) 
    change_rate= round(float(jd['priceChangePercent']), 2) 
    if change_rate < 0:
        up_down = '跌'
    else :
        up_down = '漲'
    localtime= str((datetime.datetime.now()) + datetime.timedelta(hours = 8))
    HMS= (localtime[11:19])

    final_part=str(f"{HMS} {name} \n價格:{currentPrice}, \n{up_down}{different}({change_rate}%)")
    return final_part

