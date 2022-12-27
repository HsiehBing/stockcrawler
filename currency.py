##開頭C
import pandas
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.dates as md
import pyimgur
import logging
import os
# 'Microsoft JhengHei' # "SimHei"


def Currency(msg):
#    font = FontProperties(fname="/home/ec2-user/bingbingbot/stockcrawler/.fonts/SimHei.ttf")
#    font = "AR PL UKai TW"
    
    font = FontProperties(fname=".fonts/SimHei.ttf")
#

##
    currency_name = msg[1:]
    dfs = pandas.read_html(f'https://rate.bot.com.tw/xrt/quote/ltm/{currency_name}')
    rate = dfs[0]
    rate =rate.iloc[:,0:6]
    rate.columns = ['掛牌日期', '幣別','現金-買入','現金-賣出','即期-買入','即期-賣出']
    rate['掛牌日期'] = pandas.to_datetime(rate['掛牌日期'], format = '%Y/%m/%d')

    fig =plt.figure(figsize = (10,5))
#    plt.rcParams['font.family'] = font.get_name()
#    plt.rcParams['font.family'] = ["SimHei"] #AR PL UKai CN
    plt.rcParams['axes.unicode_minus'] = False

    
    plt.plot(rate['掛牌日期'], rate['即期-買入'], label=f'即期-買入{rate.iloc[0][4]}', color = 'red')

    plt.plot(rate['掛牌日期'], rate['即期-賣出'], label=f'即期-賣出{rate.iloc[0][5]}', color = 'blue')
    plt.ylabel("price", size= 20 )
    plt.xlabel("date", size= 20)
    plt.grid(True)
    locator = md.MonthLocator()
    plt.gca().xaxis.set_major_locator(locator)
    todate = rate.iloc[0][0].strftime('%Y-%m-%d')
    plt.title(f'{todate}  {rate.iloc[0][1]}', size= 25, font_properties=font)

    plt.yticks(fontsize = 18)
    plt.xticks(fontsize = 18)
    plt.legend(loc='upper left',prop={'size': 15})

    #
    plt.savefig('send.png')
    CLIENT_ID = "b6bf473fd4d0d4c"
    PATH = "send.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="GG202201170949")
    return uploaded_image.link
