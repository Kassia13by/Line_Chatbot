#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import requests
import json
from bs4 import BeautifulSoup


#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://doc-00-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/kbjd0fbh0a1d3mkklgfishrhlo9qedv5/1661311425000/10318039330111529760/*/1zrEz1xD0kXhyId08loPkNBsiOsp_rdd1?e=view&uuid=7f539d52-5139-44de-91f1-60c3f496cc36",
        alt_text='線上購物',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #蝦皮
                link_uri="https://shopee.tw",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #momo
                link_uri="https://www.momoshop.com.tw/main/Main.jsp?cid=memb&oid=back2hp&mdiv=1099800000-bt_0_150_01-bt_0_150_01_e1&ctype=B&sourcePageType=4",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #pc home
                link_uri="https://shopping.pchome.com.tw",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #生活市集
                link_uri="https://www.buy123.com.tw",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=1000
                )
            )
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
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例

# 股市新聞
def news_crawler():
    base = "https://news.cnyes.com"
    url  = "https://news.cnyes.com/news/cat/headline"
    re   = requests.get(url)

    content = ""

    soup = BeautifulSoup(re.text, "html.parser")
    data = soup.find_all("a", {"class": "_1Zdp"})
    
    for index, d in enumerate(data):
        if index <8:
            title = d.text
            href  = base + d.get("href")
            content += "{}\n{}\n".format(title, href)
        else:
            break
        
    return content


# 即時新聞

def breaknews_crawler():
    base = "https://udn.com"
    url  = "https://udn.com/news/breaknews/1"
    re   = requests.get(url)

    content = ""

    soup = BeautifulSoup(re.text, "html.parser")
    data = soup.find_all("a", {"class": "story-list__image--holder"})
    
    for index, d in enumerate(data):
        if type(d.get('aria-label')) is str:
            if index <8:
                title = d['aria-label']
                href  = base + d.get("href")
                content += "{}\n{}\n".format(title, href)
            else:
                break
        
    return content

# 水庫
def reservoir_crawler(msg):
    url  = "https://www.taiwanstat.com/waters/latest"
    re   = requests.get(url)
    data = re.json()
    data = data[0]

    reservoir = []
    # 水庫名稱
    for d in data:
        reservoir.append(d)

    for r in reservoir:
        if msg in reservoir:
            name = data[str(msg)]["name"]
            volu = data[str(msg)]["volumn"]
            perc = data[str(msg)]["percentage"]
        else:
            continue

    content = ""
    content += f"名稱: {name}\n蓄水百分比: {perc}%\n有效蓄水量: {volu}"

    return content

# 字典

RE_api_key = 'Your reurl API'
def reurl(url):
    data = {"url": url}
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json', 'reurl-api-key': RE_api_key}
    response = requests.post(
        "https://api.reurl.cc/shorten", data=data_json, headers=headers)
    s = response.json()
    print(s['short_url'])
    return s['short_url']

target_search_temp = ""

def search(data):
    data = data.strip()
    global target_search_temp
    target_search_temp="https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXW.mI4ddaGgAMYp7rolQ;_ylc=X1MDMTM1MTIwMDM3OQRfcgMyBGZyAwRncHJpZAMEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA3R3LmRpY3Rpb25hcnkuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNARxdWVyeQN5cnJyBHRfc3RtcAMxNTY5MTM3NjE5?p=%s&fr=sfp&iscqry="%(data)
    r = requests.get(target_search_temp) #將網頁資料GET下來
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
    composing = soup.prettify() #排版 測試用
    #print(composing)
  
    web_div = soup.find(id='web') #以id搜尋 web , 搜尋結果的div
    search = web_div.find("div",class_="dd cardDesign dictionaryWordCard sys_dict_word_card")
    #print(search.prettify())

    voc_info = {} # 建立字典

    #抓單字名
    word = search.span # 抓單字名
    voc_info.update({"word":word.text})  
    #print(voc_info)

    # KK、DJ音標 
    phonetic = search.find_all("div",class_="compList d-ib")[0].find_all("span")
    #print(phonetic)
    voc_info.update({"KK":phonetic[0].text,"DJ":phonetic[1].text})
    #print(voc_info)

        #詞性、中文
    speech = search.find_all("div",class_="compList mb-25 p-rel")[0].find_all("li")
    list_speech_1 = []#詞性
    list_speech_2 = []#翻譯
    list_ans = ""
    for i in range(0,len(speech)):
        temp =speech[i].find_all("div")
        temp1 = temp[0].text#詞性
        temp2 = temp[1].text#翻譯
        list_speech_1.append(temp1)
        list_speech_2.append(temp2)
        list_ans += "("+str(i+1) + ") " + temp1 + " " + temp2 +  "\n" 
    # print(list_speech_1)
    # print(list_speech_2)

    s_url = reurl(target_search_temp)
    answer = "單字：" + voc_info["word"] + "\n" + "發音：" + voc_info["KK"] + " " + voc_info["DJ"] + "\n說明：\n" +list_ans + "\n\n資料來源：\n"+ s_url +"\nyahoo 字典"
    return answer




