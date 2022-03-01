##開頭V
import requests
import bs4
from bs4 import BeautifulSoup
import datetime

def Vitual_Currency(msg):
    vsName = msg[1:].upper()
    res = requests.get(f'https://crypto.cnyes.com/{vsName}/24h')
    soup = BeautifulSoup(res.text, "html.parser")
    script = soup.find("div").text
    #price
    currentPrice = soup.find("span",class_="jsx-143270965").text
    flt_currentPrice0 = currentPrice.replace(',','')
    flt_currentPrice = float(flt_currentPrice0)

    #name
    name = soup.find("section").text
    script0 = soup.find("section", class_="jsx-143270965 current-quote")
    script00 = script0.find("div", class_="jsx-143270965 price-change" )
    different = script00.find("span").text
    flt_different0 = different.replace(',','')
    flt_different  = float(flt_different0)
    fchange_rate = flt_different/flt_currentPrice*100
    schange_rate= (str(fchange_rate)[:4])
    if flt_different >0:
        up_down = '漲'
    elif flt_different <0:
        up_down = '跌'
    localtime= str((datetime.datetime.now()) + datetime.timedelta(hours = 8))
    HMS= (localtime[11:19])

    final_part=str(f"{HMS} {name} 價格:{currentPrice}, {up_down}{different}({schange_rate}%)")
    return final_part


