# *跟**
import matplotlib.pyplot as plt
import pyimgur
import yfinance as yf
import datetime
import matplotlib.dates as md
import pickle

def glucose_graph(msg):
    if msg[2].encode('UTF-8').isalpha()==False :
#    if msg[2] not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        a_file = open("Input.pkl", 'rb')
        Input = pickle.load(a_file)
        a_file.close()
               
        time = datetime.datetime.now()
        if msg[1]=='*':
            StockName = Input[msg[2:]]
            delate = 30
        
        else:
            StockName = Input[msg[1:]]
            delate = 120
        
#####################
        """
        plt.figure(figsize=(240,240))
        plt.plot(ug)
        plt.savefig('send.png')
        """
        plt.rcParams['font.sans-serif'] = ['SimHei']
        a_file = open("Output.pkl", 'rb')
        Output = pickle.load(a_file)
        a_file.close()
        stockNameE =Output[StockName]
    

    
        time000 = datetime.timedelta(days= -delate)
        time00= time + time000
        start = f'{time.year}-{time.month}-{time.day}'
        end = f'{time00.year}-{time00.month}-{time00.day}'
        stock = yf. download(StockName, end, start)
        
        stock.head()
        fig =plt.figure(figsize = (10,5))
        plt.plot(stock["Close"], color = "red")
        plt.ylabel("price", size= 20 )
        plt.xlabel("date", size= 20)
        plt.grid(True)
        locator = md.MonthLocator()
        plt.gca().xaxis.set_major_locator(locator)
        plt.title(f'{stockNameE} {delate}days History Price', size= 25)
        plt.yticks(fontsize = 18)
        plt.xticks(fontsize = 18)
        plt.plot()
        plt.savefig('send.png')
    # plt.show()
    # glucose_graph("*tsla") 
        CLIENT_ID = "b6bf473fd4d0d4c"
        PATH = "send.png"
        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title="GG202201170949")
        return uploaded_image.link





###################################################################################
#This part is for America stock
    else:  
        """
        plt.figure(figsize=(240,240))
        plt.plot(ug)
        plt.savefig('send.png')
        """
        
        time = datetime.datetime.now()
        ##change the word to lower
        if msg[1]=='*':
            StockName = msg[2:].lower()
            StockNameE = msg[2:].upper()
            delate = 30
        
        else:
            StockName = msg[1:].lower()
            StockNameE = msg[1:].upper()
            delate = 120
    
        time000 = datetime.timedelta(days= -delate)
        time00= time + time000
        start = f'{time.year}-{time.month}-{time.day}'
        end = f'{time00.year}-{time00.month}-{time00.day}'
        stock = yf. download(StockName, end, start)
        
        stock.head()
        fig =plt.figure(figsize = (10,5))
        plt.plot(stock["Close"], color = "red")
        plt.ylabel("price", size= 20 )
        plt.xlabel("date", size= 20)
        plt.grid(True)
        locator = md.MonthLocator()
        plt.gca().xaxis.set_major_locator(locator)
        plt.title(f'{StockNameE} {delate}days History Price', size= 25)
        plt.yticks(fontsize = 18)
        plt.xticks(fontsize = 18)
        plt.plot()
        plt.savefig('send.png')
    # plt.show()
    # glucose_graph("*tsla") 
        CLIENT_ID = "b6bf473fd4d0d4c"
        PATH = "send.png"
        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title="GG202201170949")
        return uploaded_image.link
# img_url = glucose_graph(msg)
# print(img_url)


# #畫圖與存圖的
# def glucose_graph(sid,ug):
# plt.figure(figsize=(240,240))
# plt.plot(ug)
# plt.savefig('send.png')
# CLIENT_ID = "233a2069365e"
# PATH = "send.png"
# im = pyimgur.Imgur(CLIENT_ID)
# uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
# return uploaded_image.link
# #呼叫部分
# #sid is event.message.text
# #eat is list
# img_url = glucose_graph(sid, eat)
# message = ImageSendMessage(original_content_url=img_url,preview_image_url=img_url)
# line_bot_api.push_message(to, message)