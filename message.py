#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='補充資源',
	 base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #均一國語文
                link_uri="https://www.junyiacademy.org/junyi-chinese/ele-c",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #均一數學四年級
                link_uri="https://www.junyiacademy.org/course-compare/math-elem/math-4",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #學習吧
                link_uri="https://www.learnmode.net/search?q=",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #老師的小天地
                link_uri="https://www.canva.com/design/DAFLVsU6-x0/vpHgptJink4nvSz8lro1ag/view?website#2",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=1000
                )
            ),

        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='使用教學',
        template=ConfirmTemplate(
            text="使用教學",
            actions=[
                PostbackTemplateAction(
                    label="影片教學",
                    text="現在、立刻、馬上",
                    data="影片"
                ),
                MessageTemplateAction(
                    label="文字說明",
                    text="文字說明文字說明"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='任務清單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/leN9M2e.jpg',
                    title='單元2:乘法',
                    text='請選擇較進行的活動',
                    actions=[
                        PostbackTemplateAction(
                            label='課前預習',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='課中練習',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='課後複習',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/jFNsxBY.jpg',
                    title='任務清單',
                    text='選擇目標任務',
                    actions=[
                        PostbackTemplateAction(
                            label='注意事項',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='開始！！！',
                            text='你決定要開始～'
                        ),
                        URITemplateAction(
                            label='使用回饋',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='解題小幫手',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/5rnnEKZ.jpg",
                    action=URITemplateAction(
                        label="進位紀錄",
                        uri="https://i.imgur.com/5rnnEKZ.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/9JTIUbi.jpg",
                    action=URITemplateAction(
                        label="進位加法",
                        uri="https://i.imgur.com/9JTIUbi.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/qlGNUB4.jpg",
                    action=URITemplateAction(
                        label="整數倍規律",
                        uri="https://i.imgur.com/qlGNUB4.jpg"
                    )
                ),
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例
