from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from yfinaince import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import yfinance as yf
import matplotlib.pyplot as plt
import pyimgur

#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('T5Zqw8jYWPqLTdpT46lz06Wbqm3RpDw3mrylWdKdV5YRUXqXw/I4BW1Mmp/M0VgK3kA5r4v/V9r4cH2/gH2PIM46uLoHraHb2DxW8EB8lrPT2GzH1YLgETJ8MDuomMwbeDhk/2T4CUM9RxXC3K1E3AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fb51bfd54e6dca9668655d34b92ebb71')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '#' in msg:
        message =TextSendMessage(finainces(msg)) 
        line_bot_api.reply_message(event.reply_token, message)

    elif '*' in msg:
         StockName = msg[1:]
         Ticker2 = yf.Ticker(StockName)
         message = TextSendMessage(text=str( Ticker2.info['previousClose'] ) )
         line_bot_api.reply_message(event.reply_token, message)
    elif 'P' in msg:
        client.replyMessage(event.replyToken, 
        {
        type: 'image',
        originalContentUrl: 'https://i.imgur.com/cnqrFHa.png',
        previewImageUrl: 'https://i.imgur.com/cnqrFHa.png'
        }
        )
        
    

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
