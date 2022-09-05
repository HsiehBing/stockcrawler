import requests
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd
import pyimgur
import matplotlib.dates as md
import pickle
from datetime import timedelta
from bs4 import BeautifulSoup
import numpy as np
def today_price_test(msg):            
    font = FontProperties(fname=".fonts/SimHei.ttf")    
    url_1 = "https://tw.quote.finance.yahoo.net/quote/q?type=tick&perd=1m&mkt=10&sym=%23001&callback=jQuery111306542881972874997_1662122335842&_=1662122335843"
    url_2 = 'https://tw.quote.finance.yahoo.net/quote/q?type=tick&perd=1m&mkt=10&sym=%23001&callback=jQuery111301426021457469553_1644243086726&_=1644243086727'
    indexNameE = '上市指數'
    res = requests.get(url_1)
    text_get = res.text
    #資料整理
    pos_n = text_get.index("tick", text_get.index("tick")+1)
    data = text_get[pos_n+7:-4]
    plt.rcParams['figure.facecolor']='white'
    font = FontProperties(fname=".fonts/SimHei.ttf")
    edge_fmin = 60
    dt = pd.DataFrame(eval(data))
    dt.index = pd.to_datetime(dt['t'].astype(str),format= '%Y%m%d%H%M' )
    pltx = np.arange(len(dt))
    fig,axs = plt.subplots(2, 1, gridspec_kw={'width_ratios': [2],'height_ratios': [4, 1]} ,sharex = True)

    axs[0].plot(pltx,dt.p, color = 'blue')
    axs[0].tick_params('x',length = 0)
    axs[0].sharex(axs[1])
    axs[0].spines['bottom'].set_visible(False)
    axs[0].axhline(y = dt['p'][0], color = 'black')
    axs[0].set_ylim((dt['p'][0])*0.97, (dt['p'][0])*1.03)
    axs[0].grid()

    axs[1].bar(pltx,dt.v,facecolor = 'red')
    axs[1].set_xticks(pltx[::30])
    axs[1].set_xticklabels(dt.index[::30].strftime('%H:%M'))
    axs[1].spines['top'].set_visible(False)
    axs[1].grid()
    axs[1].set_xlim(pltx[0],pltx[-1])
    plt.subplots_adjust(hspace = 0.0)
    #########
    #標註最高點與最低點
    close_nN = list(filter(None, dt.p))
    max_element = max(close_nN)
    min_element = min(close_nN)

    # x_maxedge = dt.index[20].strftime('%H:%M') -  dt.index[0].strftime('%H:%M')
    ##最高點
    max_indx = close_nN.index(max_element)
    x_max_value = dt.index[max_indx].strftime('%H:%M')
    y_max_value = dt.p[max_indx]
    # x_maxedge = max(dt['t'])-10
    # if x_max_value > x_maxedge:
    #     x_max_value = x_max_value-60

    ##最低點
    min_index = close_nN.index(min_element)
    x_min_value =  dt.index[min_index].strftime('%H:%M')
    y_min_value =  dt.p[min_index]
    if min_index > 250:
        min_index = min_index-30

    ##標註
    axs[0].annotate(int(max_element), xy = (pltx[max_indx], y_max_value), color = 'red', size=18, fontproperties = font)
    axs[0].annotate(int(min_element), xy = (pltx[min_index],y_min_value-edge_fmin), color = 'blue', size=18, fontproperties = font)
    #check the postive and negtive
    # plt.rcParams['axes.unicode_minus'] = False
    ##畫前一天開盤價


    #########
    #爬取今天資料
    res = requests.get(url_2)
    soup = BeautifulSoup(res.text, "html.parser").text
    sChange_Rate =(dt["p"][-1]-dt["p"][-2]) /dt["p"][0]
    Current_Point = dt["p"][-1]
    Change_Point = dt["p"][-1]-dt["p"][-2]
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
    plt.figtext(0.1, 0.89, titleB, fontsize=18,fontproperties = font, color=get_color, ha ='left', )
    plt.savefig('send.png')
    CLIENT_ID = "b6bf473fd4d0d4c"
    PATH = "send.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="GG202201170949")
    return uploaded_image.link


