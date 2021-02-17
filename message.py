#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='活動',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #HC FB網站
                link_uri="https://www.facebook.com/happytocoding",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #HC官方網站
                link_uri="https://www.happycoding.today/",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #HC IG
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #塔吉特千層蛋糕
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #亞尼克生乳捲
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
    )
    return message


#關於LINEBOT聊天內容範例