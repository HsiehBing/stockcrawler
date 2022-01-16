from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from yfinaince import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import yfinance as yf
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
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif '#' in msg:
        
        #def finainces():
        #    return '123'
###################
        #  message = finainces()
###################
        message =TextSendMessage(finainces(msg)) 
        
        
        
        # #message = TextSendMessage(text=f"現在股價, {str( Ticker.info['currentPrice'] )} ")
        line_bot_api.reply_message(event.reply_token, message)
###################
    elif '*' in msg:
         StockName = msg[1:]
         Ticker2 = yf.Ticker(StockName)
        # message = TextSendMessage(text=str( yfinance.Price( 'tsla' ) ) )
         message = TextSendMessage(text=str( Ticker2.info['previousClose'] ) )
         line_bot_api.reply_message(event.reply_token, message)

       
    else:
        message = TextSendMessage(text="輸入錯誤")
        line_bot_api.reply_message(event.reply_token, message)
    

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
