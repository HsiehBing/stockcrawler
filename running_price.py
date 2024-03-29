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
import numpy as np


def today_price(msg):
    msg = msg[1:]
    Name = ('TSE', '大盤',  'OTC', '上櫃')
    TSE_i = ('TSE', '大盤')
    OTC_i =('OTC','上櫃')
    up_down=[]
    get_color=[]
    font = FontProperties(fname=".fonts/SimHei.ttf")
    if msg in Name:        
#         rul_1 = []
#         url_2=[]
#         indexNameE = []
#         edge_fmin =[]
        #變數設定
        if msg in TSE_i:
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
        font = FontProperties(fname=".fonts/SimHei.ttf")    
        res = requests.get(url_1)
        text_get = res.text
        #資料整理
        pos_n = text_get.index("tick", text_get.index("tick")+1)
        data = text_get[pos_n+7:-4]
        plt.rcParams['figure.facecolor']='white'
        font = FontProperties(fname=".fonts/SimHei.ttf")
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

        axs[1].set_xlim(0 , 270)
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
        sChange_Rate =(dt["p"][-1]-dt["p"][0]) /dt["p"][0]
        Current_Point = dt["p"][-1]
        Change_Point = dt["p"][-1]-dt["p"][0]
        Point_Gap = round(float(Change_Point),2)
        Change_Rate = round(float(sChange_Rate*100),2)
        if Point_Gap >0:
            up_down = '漲'
            get_color = 'red'
        elif Point_Gap <0:
            up_down = '跌' 
            get_color = 'green'
        else:
            up_down =''
            get_color = 'black'
        ##股價跟漲跌幅
        titleA = indexNameE
        titleB = f'{Current_Point}  {up_down}{Point_Gap}({Change_Rate}%)'
    ############################################
    else:
    ##輸入的訊息轉成代號
        a_file = open("Input.pkl", 'rb')
        Input = pickle.load(a_file)
        a_file.close()       
        stockName = Input[msg]
    #######編碼問題尚待解決    
        a_file2 = open("Output.pkl", 'rb')
        Output = pickle.load(a_file2)
        a_file.close()
    #輸出股價名稱
        stockNameE = Output[stockName]
    ########################
    ########################
    #爬當日股價
        res = requests.get(f'https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;autoRefresh=1642576273209;symbols=["{stockName}"];type=tick?bkt=&device=desktop&ecma=modern&feature=ecmaModern,useVersionSwitch,useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=anhj1hpgufeaf&region=TW&site=finance&tz=Asia/Taipei&ver=1.2.1214&returnMeta=true')
        jd = res.json()['data']
        meta =(jd[0]['chart']['meta'])
        PreviousClose =(jd[0]['chart']['meta']['previousClose'])
        Previous_Price =round((meta['previousClose']),2)
        Current_Price = round((meta['regularMarketPrice']),2)
        Price_Gap = round((Current_Price-Previous_Price),2)
        Change_Rate = round((Price_Gap/Previous_Price*100),2)
        if Price_Gap >0:
            up_down = '漲'
            get_color = 'red'
        elif Price_Gap <0:
            up_down = '跌'
            get_color = 'green'
        else:
            up_down = ""
            get_color = 'black'
    #取位數調整
        Today_upper = PreviousClose*1.1
        Today_bottom = PreviousClose*0.9
    #收盤價
        close =  jd[0]['chart']['indicators']['quote'][0]['close']
    #時間
        timestep =jd[0]['chart']['timestamp']
        df = pd.DataFrame({'timestamp': timestep, 'close': close})
        df.head()
        df['dt'] = pd.to_datetime(df['timestamp']+ 3600 * 8, unit='s')
    #畫圖
        fig1 = plt.figure()
        ax = fig1.add_axes([0.1, 0.1, 0.75, 0.75])
        ax =df.plot('dt', 'close', ax=ax)
        ax.set_ylim(Today_bottom, Today_upper)
        plt.xticks(fontsize = 12)
        plt.yticks(fontsize = 12)
    ########################
    ####畫前役天收盤價
        ax.set_xlim(pd.Timestamp('09:00'),pd.Timestamp("13:30"))
    ########################
        majorFmt = md.DateFormatter('%H:%M')   ## 畫x時間
        ax.xaxis.set_major_locator(md.MinuteLocator(byminute = [0,30]))
        ax.xaxis.set_major_formatter(majorFmt)

    #標註最高點與最低點
        close_nN = list(filter(None, close))
        max_element = max(close_nN)
        min_element = min(close_nN)
        ###
        if max_element != min_element:
            max_indx = close.index(max_element)
            x_max_value = df['dt'][max_indx]
            y_max_value = close[max_indx] 
            x_maxedge = max(df['dt'])+timedelta(minutes=-30)
            if x_max_value > x_maxedge:
                x_max_value = x_max_value+timedelta(minutes=-40)
            if y_max_value > PreviousClose*1.08:
                y_max_value = y_max_value - PreviousClose*0.02

            min_index = close.index(min_element)
            x_min_value =  df['dt'][min_index]
            y_min_value =  close[min_index] - PreviousClose*0.015
            x_minedge = max(df['dt'])+timedelta(minutes=-30)
            if x_min_value > x_minedge:
                x_min_value = x_min_value+timedelta(minutes=-40)
            if y_min_value < PreviousClose * 0.9 :
                y_min_value = y_max_value + PreviousClose*0.02


            ax.annotate(max_element, xy = (x_max_value,y_max_value), color = 'red', size=18, fontproperties = font)
            ax.annotate(min_element, xy = (x_min_value,y_min_value), color = 'blue', size=18, fontproperties = font)
        else:
            ax.annotate(min_element, xy = (x_min_value,y_min_value), color = 'black', size=18)
        ###
        #check the postive and negtive
        plt.rcParams['axes.unicode_minus'] = False

        ##畫前一天開盤價
        plt.axhline(y=PreviousClose, xmin=0, xmax=1, color='black')

        ##標上股價跟漲跌幅
        titleA = stockNameE
        titleB = f'{Current_Price}  {up_down}{Price_Gap}({Change_Rate}%)'
        ax.grid(bool)
        ax.set_xlabel('')
        ax.legend('')
        
    ##標上
    plt.rcParams['axes.unicode_minus'] = False
    plt.figtext(0.1, 0.94, titleA, fontsize=18,fontproperties = font, color='black', ha ='left', )
    plt.figtext(0.1, 0.88, titleB, fontsize=18,fontproperties = font, color=get_color, ha ='left', )
   ########################

    #輸出圖
    plt.savefig('send.png')
    CLIENT_ID = "b6bf473fd4d0d4c"
    PATH = "send.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="GG202201170949")
    return uploaded_image.link