from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
import sys
import traceback
import time
import random
import re

api_id = 4062721  #apiid
api_hash = '0cc4c87e15241c0b7267d74b211ef358'  #apihash
phone = '+84924728421'  #telegram phonenr


timer = 10 #delay in seconds, aka how long you want to wait before sending a msg again
msgtosend = """🌘🌘CloneBit Project🌘🌘





Hold CloneBit tokens and earn Uniswap Token!




5% in Uni while buying and 12% in Uni while selling!







Telegram : @clonebitofficialcommunity



Telegram announcement : @clonebitannouncementsofficial



Twitter : http://twitter.com/Clonebitproject



Website : https://clonebit.space/

""" # MESSAGE TO SEND
#here you can either replace message to send w a filelocation .txt, but i want to keep everything in one place so i use a text to one line converter soruce: https://lingojam.com/TexttoOneLine

# these functions here use your api and api hash to connect to your telegram account.
client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
#

chats = []
last_date = None
amountofgroups = 100 #count the amount of groups your shillaccount has joined and put the amount there.
groups=[] # if you really want to specify the groups you want to send to you can write them inside their, otherwise it will send to all of them

result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=amountofgroups,
                hash = 0
            ))
            
chats.extend(result.chats)
for chat in chats:
    try:
        groups.append(chat)
    except:
        continue
while True:    
    for group in groups:
        try:
            username1 = group.username
            print(username1)    
            client.send_message(username1, msgtosend)
            time.sleep(1)
        except:
            continue 
    print("Shill Wave Complete!!, Delay " + str(timer) + " seconds")
    time.sleep(timer)
