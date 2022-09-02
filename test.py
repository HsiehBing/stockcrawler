#盤中即時行情
#代號P
import requests
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd
import pyimgur
import matplotlib.dates as md
import pickle
from datetime import timedelta
from bs4 import BeautifulSoup


def today_price_test(msg):
    msg = msg[1:]
    Name = ('TSE', '大盤',  'OTC', '上櫃')
    TSE_i = ('TSE', '大盤')
    OTC_i =('OTC','上櫃')
    up_down=[]
    get_color=[]
    font = FontProperties(fname=".fonts/SimHei.ttf")
    if msg == "TSE":
        url_1 = "https://tw.quote.finance.yahoo.net/quote/q?type=tick&perd=1m&mkt=10&sym=%23001&callback=jQuery111306542881972874997_1662122335842&_=1662122335843"
        url_2 = 'https://tw.quote.finance.yahoo.net/quote/q?type=tick&perd=1m&mkt=10&sym=%23001&callback=jQuery111301426021457469553_1644243086726&_=1644243086727'
        indexNameE = '上市指數'
        edge_fmin = 30
    else:
        url_1 = 'https://tw.quote.finance.yahoo.net/quote/q?type=tick&perd=1m&mkt=10&sym=%23026&callback=jQuery11130041106533656785293_1662132769586&_=1662132769587'
        url_2 = 'https://tw.quote.finance.yahoo.net/quote/q?type=tick&perd=1m&mkt=10&sym=%23026&callback=jQuery1113011660253264229259_1644245704375&_=1644245704376'
        indexNameE = '上櫃指數'
        edge_fmin = 1

    #從網路爬取資料
    res = requests.get(url_1)
    text_get = res.text
    #資料整理
    pos_n = text_get.index("tick", text_get.index("tick")+1)
    data = text_get[pos_n+7:-4]
    data = data.split(",")
    get_time = []
    get_price = []
    get_volumn = []
    for i in range(len(data)):
        if i %3 == 0:
            get_time.append(int(data[i][13:]))
        elif i%3 == 1:
            get_price.append(float(data[i][4:]))
        else :
            get_volumn.append(data[i][4:-1])
    df = pd.DataFrame({'timestamp': get_time, 'close': get_price})
    #走勢圖的上下限
    Previous_Price = get_price[0]
    Today_bottom = Previous_Price * 0.97
    Today_upper =  Previous_Price * 1.03
    #畫圖
    df.head()
    fig1 = plt.figure()
    ax = fig1.add_axes([0.1, 0.1, 0.75, 0.75])
    ax =df.plot('timestamp', 'close', ax=ax)
    ax.set_ylim(Today_bottom, Today_upper)
    ax.set_xlim(900, 1330)
    plt.xticks( fontsize = 12)
    plt.yticks(fontsize = 12)
    ax.grid(bool)
    ax.set_xlabel('')
    ax.legend('')
    #標註最高點與最低點
    close_nN = list(filter(None, get_price))
    max_element = max(close_nN)
    min_element = min(close_nN)
    ##最高點
    max_indx = get_price.index(max_element)
    x_max_value = df['timestamp'][max_indx]
    y_max_value = get_price[max_indx]
    x_maxedge = max(df['timestamp'])-10
    if x_max_value > x_maxedge:
        x_max_value = x_max_value-60
    ##最低點
    min_index = get_price.index(min_element)
    x_min_value =  df['timestamp'][min_index]
    y_min_value = get_price[min_index]
    x_minedge = max(df['timestamp'])-10
    if x_min_value > x_minedge:
        x_min_value = x_min_value-60
    ##標註
    ax.annotate(int(max_element), xy = (x_max_value,y_max_value), color = 'red', size=18, fontproperties = font)
    ax.annotate(int(min_element), xy = (x_min_value,y_min_value-edge_fmin), color = 'blue', size=18, fontproperties = font)
    #check the postive and negtive
    plt.rcParams['axes.unicode_minus'] = False
    ##畫前一天開盤價
    plt.axhline(y= get_price[0], xmin=0, xmax=1, color='black')

    #爬取今天資料
    res = requests.get(url_2)
    soup = BeautifulSoup(res.text, "html.parser").text
    sChange_Rate = (soup[soup.find('"185"')+6:soup.find('"443"')-1])
    Current_Point = (soup[soup.find('"125"')+6:soup.find('"126"')-1])
    Change_Point = (soup[soup.find('"184"')+6:soup.find('"185"')-1])
    Point_Gap = round(float(Change_Point),2)
    Change_Rate = round(float(sChange_Rate),2)
    if Point_Gap >0:
        up_down = '漲'
        get_color = 'red'
    elif Point_Gap <0:
        up_down = '跌' 
        get_color = 'green'
    ##股價跟漲跌幅
    titleA = indexNameE
    titleB = f'{Current_Point}  {up_down}{Point_Gap}({Change_Rate}%)'
    ##標上
    plt.rcParams['axes.unicode_minus'] = False
    plt.figtext(0.1, 0.94, titleA, fontsize=18,fontproperties = font, color='black', ha ='left', )
    plt.figtext(0.1, 0.88, titleB, fontsize=18,fontproperties = font, color=get_color, ha ='left', )
   ########################
    ax.grid(bool)
    ax.set_xlabel('')
    ax.legend('')
    #輸出圖
    plt.savefig('send.png')
    CLIENT_ID = "b6bf473fd4d0d4c"
    PATH = "send.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="GG202201170949")
    return uploaded_image.link
    ############################################