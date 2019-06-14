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
    if msg in ['hi', 'Hi', '你好']:
        r = '你好~今天運動沒'

    elif msg in ['還沒', '等等就去', '今天有點懶', '不想運動', '明天再去']:
        r = '不要偷懶啦!!!!快去運動吧'

    elif msg in ['我想運動', '好想運動啊!', '好想運動']:
        r = '快來看看新的運動資訊' + '\n' + 'https://paendless.wixsite.com/mysite/blog'
    elif msg in ['怎麼聯絡你們?', '我想找客服', '我要投訴']:
        r = '點我~' + '\n' + 'https://paendless.wixsite.com/mysite/blank-1'
    elif msg in ['我想成為分享者']:
        r = '點我~' + '\n' + 'https://paendless.wixsite.com/mysite/writer'
    elif msg in ['我今天心情不好', '陪我聊天', '覺得無聊']:
        r = '想聊點什麼嗎~'
    elif '問題' in msg:
        r = '點我~' + '\n' + 'https://paendless.wixsite.com/sharer/blank-2'

    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()