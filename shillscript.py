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
msgtosend = """🌘Welcome to The DarkMoon Project🌘

🌘DarkMoon formed during a collision between the BTC Planet and another small planet SafeMoon! Rewarding holders with 10% in BTC to the DarkMoon Lovers and with the liquidity burnt to provide the holders with a happy sleep watching the Moon thinking about DarkMoon!

🌘We strive to create a Project on Binance Smart Chain which offers the following:
✔️Low Transaction Fee
✔️SAFU
✔️10% BTC Rewards to the Holders

🌘SMART CONTRACTS : https://bscscan.com/token/0x92D9fbf6C7e3dfE6A57E1A553704D2a91BC97b73

🌘BUY HERE : https://exchange.pancakeswap.finance/#/swap?outputCurrency=0x92D9fbf6C7e3dfE6A57E1A553704D2a91BC97b73

🌘LP BURN : https://bscscan.com/tx/0x0f1176fb427d551511526e52fa6a7b76fbbe9d2e052b439ab2da19eaff63b451

🌘CHART : https://poocoin.app/tokens/0x92D9fbf6C7e3dfE6A57E1A553704D2a91BC97b73

Telegram Official : https://t.me/DarkMoon_project
Website : https://darkmoonproject.space/
Twitter : https://twitter.com/DarkMoon_real""" # MESSAGE TO SEND
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
amountofgroups = 22 #count the amount of groups your shillaccount has joined and put the amount there.
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
