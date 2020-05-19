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
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
from cv2 import cv2
import numpy as np
#======python的函數庫==========

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('ZbWIGQOfoxOLqko0Fhh/OTjBMeeXrd+Py4xyAaNeFsa0bVP3vY05ZyOZEVj8cS9Zu+PDXGMfIUDzAGhFEjHVMN8J9ocEZsuGotbuRhzeQTML221ynVdVwXntBcIP4Ft+Sy0omAoemN84m8OxTJbFWQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('eeed6c17319b3f197e255e08bc2e98c3')

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
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(MessageEvent, message=(ImageMessage))
def handle_message(event):
    #如果LINE用戶端傳送過來的是圖片
    if isinstance(event.message, ImageMessage):
        print('收到圖片訊息')
        hull_list = []
        position_0_x = []
        position_0_y = []
        position_5_x = []
        position_5_y = []
        image_content = line_bot_api.get_message_content(event.message.id)
        with open('temp_img.jpg','rb') as f:
            img_binary = f.read()
            o = cv2.imdecode(np.frombuffer(img_binary,np.uint8),cv2.IMREAD_COLOR)#二進位資料轉成數組array，讓圖片可以用cv讀取得到並且進行處理
            gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
            ret,binary=cv2.threshold(gray,150,255,cv.THRESH_BINARY)
            contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
            #=========劃出凸矩形並且標註其輪廓編號
            n = len(contours)
            font=cv2.FONT_HERSHEY_SIMPLEX
            for i in range(n):
                hull = cv2.convexHull(contours[i])
                M = cv2.moments(hull)
                #print(i,M['m00'])
                if M['m00'] > 80 and M['m00']<450:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    print('cx的座標',cx,'cy的座標',cy)
                    if cx<300 and cx>100:
                        if cy>1850 and cy<2300:
                            print(cx,cy)
                            position_0_x.append(cx)
                            position_0_y.append(cy)
                            cv2.putText(o,'o',(cx,cy),font,1,(0,0,255),3)#p=每個像素幾公分     
                    if cx<800 and cx>600:
                        if cy>1850 and cy<2300:
                            print(cx,cy)
                            position_5_x.append(cx)
                            position_5_y.append(cy)
                            cv2.putText(o,'o',(cx,cy),font,1,(0,0,255),3)#p=每個像素幾公分
                    print(position_0_x,position_0_y)
                    print(position_5_x,position_5_y)
    #                cv2.putText(o,'o',(cx,cy),font,1,(0,0,255),3)#p=每個像素幾公分

                if M['m00'] > 100000 and M['m00']<500000:
                    print('面積',M['m00'])
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    #print('cx,cy',cx,cy)
                    cv2.polylines(o,[hull],True,(0,255,0),3)
                    #cv.drawContours(o, [box], 0, (255, 0, 0), 1)
                    #print('hull['+str(i)+']面積=',int(cv.contourArea(hull)))
                    #print('hull['+str(i)+']長度=',int(cv.arcLength(hull,True)))
                    n=len(hull)
                    for coordinate in hull:
                        #print(coordinate[0])
                        hull_list.append(tuple(coordinate[0]))
                        '''最佳擬合直線
                        rows,cols = gray.shape[:2]
                        [vx,vy,x,y]=cv.fitLine((contours[i]),cv.DIST_L2,0,0.01,0.01)
                        lefty=int(-x*vy/vx)+y
                        righty=int(((cols-x)*vy/vx)+y)
                        cv.line(o,(cols-1,righty),(0,lefty),(0,255,0),3)
                        '''
            #=========劃出凸矩形並且標註其輪廓編號==========
            y=[]      
            for point in hull_list:
                #print(point[0])
                #print(point[1])
                y.append(point[1])
            #print('min(y)',min(y))
            #print('max(y)',max(y))
            print(max(y)-min(y))
            p=5/(position_5_x[0]-position_0_x[0])
            #print(p)
            cm=round((max(y)-min(y))*p,2)
            print("穗長%scm"%(cm))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
