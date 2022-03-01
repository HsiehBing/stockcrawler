#盤中即時行情
import requests
import bs4
from bs4 import BeautifulSoup
import pickle
import re
def sTrendTrad(msg):

    a_file = open("r_Input.pkl", 'rb')
    Input = pickle.load(a_file)
    a_file.close()
    msg = Input[msg[1:]]
    StockNum = msg

    a_file = open("r_Output.pkl", 'rb')
    Output = pickle.load(a_file)
    a_file.close()
    StockNameE = Output[StockNum]


    res = requests.get(f'https://tw.stock.yahoo.com/quote/{StockNum}/institutional-trading')
    soup = BeautifulSoup(res.text, "html.parser")
    #print(soup.prettify())  #輸出排版後的HTML內容
    script = soup.find("script", text=re.compile("root.App.main")).text
    #print(script)

    ##update time
    times = script[script.find('updatedTs')+12:script.find('updatedTs')+22]
    TrendTrade_start = script.find("trendTrade")
    TrendTrade_end   = script.find('ytms')
    TrendTrad = (script[TrendTrade_start+12:TrendTrade_end-4])
    #print(TrendTrad)

    #print(times)
    foreign =TrendTrad[TrendTrad.find('foreign'):TrendTrad.find('dealer')-2]
    dealer =TrendTrad[TrendTrad.find('dealer'):TrendTrad.find('investmentTrust')-2]
    investmentTrust = TrendTrad[TrendTrad.find('investmentTrust'):TrendTrad.find('total')-2]
    total = TrendTrad[TrendTrad.find('total'):]

    foreign_E =foreign[foreign.find('text')+6:foreign.find('trend')-2]
    dealer_E =dealer[dealer.find('text')+6:dealer.find('trend')-2]
    investmentTrust_E =investmentTrust[investmentTrust.find('text')+6:investmentTrust.find('trend')-2]
    total_E =total[total.find('text')+6:total.find('trend')-2]

    foreign_C =foreign[foreign.find('change')+9:-2]
    dealer_C =dealer[dealer.find('change')+9:-2]
    investmentTrust_C =investmentTrust[investmentTrust.find('change')+9:-2]
    total_C =total[total.find('change')+9:-1]
    final_part = str(f'{times}\n{StockNameE}\n外資:{foreign_E}{foreign_C}\n投信:{investmentTrust_E}{investmentTrust_C}\n自營商:{dealer_E}{dealer_C}\n三大法人:{total_E}{total_C}')
    return final_part
