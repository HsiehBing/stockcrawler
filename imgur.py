import matplotlib.pyplot as plt
import pyimgur
import yfinance as yf
import datetime
import matplotlib.dates as md

def glucose_graph(msg):
      
    """
    plt.figure(figsize=(240,240))
    plt.plot(ug)
    plt.savefig('send.png')
    """
    time = datetime.datetime.now()
    if msg[1]=='1':
        StockName = msg[2:]
        delate = 30
     
    else:
         StockName = msg[1:]
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
    plt.title(f'{StockName} {delate}days History Price', size= 25)
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