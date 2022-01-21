#盤中即時行情
import requests
import matplotlib.pyplot as plt
import pandas
import pyimgur
import matplotlib.dates as md
def today_price(msg):
    
    stockName = f'"{msg[1:]}"'
    res = requests.get(f'https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;autoRefresh=1642576273209;symbols=[{stockName}];type=tick?bkt=&device=desktop&ecma=modern&feature=ecmaModern,useVersionSwitch,useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=anhj1hpgufeaf&region=TW&site=finance&tz=Asia/Taipei&ver=1.2.1214&returnMeta=true')
    jd = res.json()['data']
    PreviousClose =(jd[0]['chart']['meta']['previousClose'])
    #取位數調整
    Today_upper = PreviousClose*1.1
    Today_bottom = PreviousClose*0.9
    #收盤價
    close =  jd[0]['chart']['indicators']['quote'][0]['close']
    #時間
    timestep =jd[0]['chart']['timestamp']

    df = pandas.DataFrame({'timestamp': timestep, 'close': close})
    print(type(close))
    df.head()
    df['dt'] = pandas.to_datetime(df['timestamp']+ 3600 * 8, unit='s')
    
    ax =df.plot('dt', 'close')
    ax.set_ylim(Today_bottom, Today_upper)
    ax.set_xlim(pandas.Timestamp('09:00'),pandas.Timestamp("13:30"))
    majorFmt = md.DateFormatter('%H:%M')   
    ax.xaxis.set_major_locator(md.MinuteLocator(byminute = [0,30]))
    ax.xaxis.set_major_formatter(majorFmt)
    ax.set_title(stockName, size=15)
    ax.grid(bool)
    ax.set_xlabel('')
    ax.legend('')

    plt.savefig('send.png')
# plt.show()
# glucose_graph("*tsla") 
    CLIENT_ID = "b6bf473fd4d0d4c"
    PATH = "send.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="GG202201170949")
    return uploaded_image.link



