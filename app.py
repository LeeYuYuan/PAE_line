from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('VrinLe+lNFxs8L1VJJbU+NLPVUx3OrnTaOq7t1InIAQ6IohbBJiUGlGR1v4X7X9Rko61a5TWt51XIxaP9HBZOWhS2Pe5mPafYLqeJYLvjDq93dK3DH2D6SbxpIYQOPIye4/yVg6Z/vjsMegj2ImIPAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('de482eb516e18a7f8e5f72f198bcda26')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = 'hi'

    if '好懶喔' in msg:
        sticker_message = StickerSendMessage(
            package_id='11539',
            sticker_id='52114142'
        )

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message) 

        return

    count = 0
    if 'hi' in msg:
        r = '你好~今天運動沒'
    elif 'Hi' in msg:
        r = '你好~今天運動沒'    
    elif '妳好' in msg:
        r = '您好~今天運動沒'
    elif '不想運動' in msg:
        r = '快去運動RRRRR'
    elif '懶' in msg:
        r = '不要偷懶啦!!!!快去運動吧'

    elif '想運動' in msg:
        r = '快來看看新的運動資訊' + '\n' + 'https://paendless.wixsite.com/mysite/blog'
    elif '聯絡' in msg:
        r = '點我~' + '\n' + 'https://paendless.wixsite.com/mysite/blank-1'
    elif '投訴' in msg:
        r = '點我~' + '\n' + 'https://paendless.wixsite.com/mysite/blank-1'
    elif '分享者' in msg:
        r = '點我~' + '\n' + 'https://paendless.wixsite.com/mysite/writer'
    elif msg in ['我今天心情不好', '陪我聊天', '覺得無聊']:
        r = '想聊點什麼嗎~'
    elif '問題' in msg:
        r = '點我~' + '\n' + 'https://paendless.wixsite.com/sharer/blank-2'
    elif '訓練' in msg:
        r = '點我~' + '\n' +'https://paendless.wixsite.com/mysite/copy-of'
    elif '營養' in msg:
         r = '點我~' + '\n' +'https://paendless.wixsite.com/mysite/copy-of-5'
    elif '治療' in msg:
        r = '點我~' + '\n' +'https://paendless.wixsite.com/mysite/copy-of-2'
    elif '復健' in msg:
        r = '點我~' + '\n' +'https://paendless.wixsite.com/mysite/copy-of-2'
    elif '酸' in msg:
        r = '點我~' + '\n' +'https://paendless.wixsite.com/mysite/copy-of-2'
    elif '痛' in msg:
        r = '點我~' + '\n' +'https://paendless.wixsite.com/mysite/copy-of-2'
    elif '增肌' in msg:
        r = '點我~' + '\n' +'https://paendless.wixsite.com/mysite/blank-3'
    elif '減肥' in msg:
        r = '點我~' + '\n' +'https://paendless.wixsite.com/mysite/blank-8'
    elif '減脂' in msg:
        r = '點我~' + '\n' +'https://paendless.wixsite.com/mysite/blank-8'
    elif '碩文' in msg:
        r = '超肥!~~~小雞雞'
    elif '佩蓉' in msg:
        r = '漂釀~~漂釀~~'
    elif '冠綸' in msg:
        r = '阿喲!~重訓有成喔小雞雞'
    elif '建宇' in msg:
        r = '加油點好嗎'



    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()