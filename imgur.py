import matplotlib.pyplot as plt
import pyimgur
import yfinance as yf


def glucose_graph():
    """
    plt.figure(figsize=(240,240))
    plt.plot(ug)
    plt.savefig('send.png')
    """

    stock = yf. download("GooG", "2020-09-15", "2020-09-25")
    stock.head()
    fig =plt.figure(figsize = (10,5))
    plt.plot(stock["Open"], color = "red")
    plt.ylabel("price", size= 20 )
    plt.xlabel("date", size= 20)
    plt.grid(True)
    plt.title("Google open price", size= 25)
    plt.plot()
    plt.savefig('send.png')
      
    CLIENT_ID = "b6bf473fd4d0d4c"
    PATH = "send.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="GG202201170949")
    return uploaded_image.link
img_url = glucose_graph()
print(img_url)


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