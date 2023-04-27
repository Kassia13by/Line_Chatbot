from asyncio import events
from flask import Flask, request, abort, render_template

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *



#======這裡是呼叫的檔案內容=====
from message import *

#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import requests
from bs4 import BeautifulSoup
import json
import re


#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('x/SWmtn+pcO+U/6y2cmXz/VpX8V5OW0ZMHgHxftHYNUXtacCGxhGoZ3ipfuXGFppvyRJ+LWlKdGdkg4pZGzVDuPKxaSyyuf7G9vOVkT6v7UMz1YINLtUTAUgZMdIr/5RTEDOthu+yRyQy4iCQLKmqwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('5da3a0ae4f8c0f69865d940b081e2dd0')


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
    if '線上購物' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '股市新聞' in msg:
        result = news_crawler()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result))
    elif '即時新聞' in msg:
        result = breaknews_crawler()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result))
    elif '水情' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = '全台水庫資訊',
                contents = json.load(open('reservoir.json', 'r', encoding='utf-8'))
            )
        )
    elif "水庫" in msg:
        result = reservoir_crawler(msg)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )

    elif "使用說明" in msg:
        reply_message = "感謝您的訊息！\n輸入格式：\n1. 輸入「線上購物」：將提供一些線上購物連結\n2. 輸入「水情」：將提供各個水庫的蓄水量（也可直接輸入欲查詢的水庫名稱）\n3. 輸入「即時新聞」：將提供即時新聞連結\n4. 輸入「股市新聞」：將提供股市新聞連結\n5. 輸入欲查詢的英文單字：將回傳翻譯、詞性等等資訊"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_message)
        )
    else:
        answer = search(msg)
        message = TextSendMessage(text=answer)
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
