#K
import mplfinance as mpf
import yfinance as yf
import datetime
import pickle
import pyimgur
from matplotlib.font_manager import FontProperties

def Draw_candle(msg):    
    font = FontProperties(fname=".fonts/SimHei.ttf")
    if msg[2].encode('UTF-8').isalpha()==False :
        a_file = open("Input.pkl", 'rb')
        Input = pickle.load(a_file)
        a_file.close()
               
        time = datetime.datetime.now()
        if msg[1]=='K':
            StockName = Input[msg[2:]]
            delate = 150
        
        else:
            StockName = Input[msg[1:]]
            delate = 600
        
#####################

        time000 = datetime.timedelta(days= -delate)
        time00= time + time000
        start = f'{time.year}-{time.month}-{time.day}'
        end = f'{time00.year}-{time00.month}-{time00.day}'
        stock = yf. download(StockName, end, start)
        a_file = open("Output.pkl", 'rb')
        Output = pickle.load(a_file)
        a_file.close()
        stockNameE =Output[StockName]
#######################        
        mc = mpf.make_marketcolors(up='r',
                                down='g',
                                edge='',                            
                                wick='inherit',
                                volume='inherit')
    #font  'Microsoft JhengHei'  
    #font  'SimHei'
#        s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc, rc = {'font.family': 'AR PL UKai CN'})
        s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc, rc = {'font.family': font})
        mpf.plot(stock, type='candle', style=s, ylabel='', title = stockNameE, mav = (5,10, 20,60), volume=True,savefig = 'send.png')



        CLIENT_ID = "b6bf473fd4d0d4c"
        PATH = "send.png"
        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title="GG202201170949")
        return uploaded_image.link
    else:
        time = datetime.datetime.now()
        if msg[1]=='K':
            delate = 150
            StockName = msg[2:]
        
        else:
            delate = 600
            StockName = msg[1:]
        time000 = datetime.timedelta(days= -delate)
        time00= time + time000
        start = f'{time.year}-{time.month}-{time.day}'
        end = f'{time00.year}-{time00.month}-{time00.day}'
        stock = yf. download(StockName, end, start)
        mc = mpf.make_marketcolors(up='r',
                                down='g',
                                edge='',                            
                                wick='inherit',
                                volume='inherit')
    #font  'Microsoft JhengHei'  
    #font  'SimHei'
#        s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc, rc = {'font.family':'AR PL UKai TW MBE'})
        s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc, rc = {'font.family':font})
        mpf.plot(stock, type='candle', style=s, ylabel='', title = StockName, mav = (5,10, 20,60), volume=True,savefig = 'send.png')



        CLIENT_ID = "b6bf473fd4d0d4c"
        PATH = "send.png"
        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title="GG202201170949")
        return uploaded_image.link
        
