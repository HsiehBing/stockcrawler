#代號E
import requests
import matplotlib.pyplot as plt
import pyimgur
import pandas as pd
import array
import numpy as np

def plottable(figsize,data,collabels,date_title,tbfs = 12,fp = 'WenQuanYi Micro Hei'):
    #Microsoft JhengHei
    fig, ax = plt.subplots()
    fig.set_size_inches(figsize[0], figsize[1])
    plt.rcParams['font.family'] = "WenQuanYi Micro Hei"  ## set font
    
    #### Plot table
    tb = ax.table(cellText=data.values,
              colLabels=collabels,
              loc = 'center',
              cellLoc = 'right',
              bbox=[0.05, 0, 0.9, 0.98]
              )
    tb.auto_set_font_size(False) # disable auto set font size
    tb.set_fontsize(tbfs) # set table fontsize 
    
    ## set cells facecolor and table text color
    for i in range(len(data.T)):
        tb[0,i].set_facecolor('#363636')
        tb[0,i].set_text_props(color='w')
    
    ax.axis('off') ## disable axis
    ax.set_title(f'{date_title}', fontsize = 20, loc = 'center',fontproperties = fp)
    plt.savefig('send.png', dpi=100 ,bbox_inches = 'tight') ##savefigure
    CLIENT_ID = "b6bf473fd4d0d4c"
    PATH = "send.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="GG202201170949")

    return uploaded_image
    
def enddistr(msg):
    EFurl = 'https://www.twse.com.tw/fund/TWT38U?response=json&date=&_=1644690000895'
    EDurl = 'https://www.twse.com.tw/fund/TWT44U?response=json&date=&_=1644686322595'
    ETurl = 'https://www.twse.com.tw/fund/BFI82U?response=json&dayDate=&weekDate=&monthDate=&type=day&_=1644411516792'

    msgurldict = {'EF':EFurl,'ED':EDurl,'ET':ETurl}
    res = requests.get(msgurldict[msg[:2]])
    data = res.json()
    data_title,data_all = data['title'],data['data']

    #資料處理
    if msg == 'ETSE':
        data  = pd.DataFrame(data_all)
        column_labels = ["單位名稱", "買進金額", "賣出金額", "買賣差額"]

    else:
        df_all = pd.DataFrame(data_all).iloc[:,1:6]
        buy_20 = df_all.iloc[:19,:]
        new5 = np.array([float(i.replace(',','')) for i in df_all[5]])
        index_20  = np.where(new5==min(new5))[0][0]
        sell_20 = df_all[index_20:index_20+20]

        #畫圖
        matdict = {'B':[buy_20,f'{data_title}-前20買超']
                   ,'S':[sell_20,f'{data_title}-前20賣超']}
        data = matdict[msg[-1]][0]
        data_title = matdict[msg[-1]][1]
        column_labels = ['證券代號', '證券名稱', '買進股數', '賣出股數', '買賣超股數']

    uploaded_image = plottable(
              figsize = (14, (len(data)+1)*0.4),
              data = data,
              collabels = column_labels,
              date_title = data_title,
              tbfs = 12,
              fp = 'WenQuanYi Micro Hei' ##  Microsoft JhengHei
    )

    return uploaded_image.link
