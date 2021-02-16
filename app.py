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
# from new import *
# from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========




app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('eWXxSdmlYhI3wMqMDs1srmeGW2a+/bGMKP/7jFRnEproALIDF+TVoKxUT3YGLEBwG19lhJK93GSH9K47f1bQsG0s4kY5ioe6le0O5xRQ9K1nqzqhUt4xTMUlg7Y8Yqc5tqasvrlilZiRykTBabf98wdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2888aa27a4a024de8e1ceb9fb4e3ef3d')


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
    try:
        if "粉絲團" in msg:
            message = imagemap_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif "官網" in msg:
            message = imagemap_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif "活動" in msg:
            message = imagemap_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif "FB" in msg:
            message = imagemap_message()
            line_bot_api.reply_message(event.reply_token, message)
        
    except:
        #如果非以上的選項，就會學你說話
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
