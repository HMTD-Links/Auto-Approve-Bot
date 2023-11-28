from os import path, getenv, environ
import os, time 

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:rkndeveloperDEhdhyjjvjjftSEW")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "Star_Bots_Tamil")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1001819787652"))
    ADMIN = list(map(int, getenv("ADMIN", "1391556668").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002120760645"))
    DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
    CHANNEL_ID = list(set(int(x) for x in str(getenv("CHANNEL_ID", "-1001797626445 -1001816164988 -1001562195772 -1001928370532 -1001824185044 -1001674410044 -1001849017994 -1001832085294 -1001733199020 -1001347977016 -1001715180239 -1001890039607")).split()))
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    RKN_PIC = os.environ.get("RKN_PIC", "https://graph.org/file/9853637eaaf2654ccd503.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Auto_Approve_Star_Bot")
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://telegra.ph/file/293cc10710e57530404f8.mp4").split()

    LOGO = """
╔═╗╔╦╗╔═╦╗  ╔══╗╔═╗╔╗─╔╗╔═╗╔╗─╔═╗╔═╗╔═╗╔═╗
║╬║║╔╝║║║║  ╚╗╗║║╦╝║╚╦╝║║╦╝║║─║║║║╬║║╦╝║╬║
║╗╣║╚╗║║║║  ╔╩╝║║╩╗╚╗║╔╝║╩╗║╚╗║║║║╔╝║╩╗║╗╣
╚╩╝╚╩╝╚╩═╝  ╚══╝╚═╝─╚═╝─╚═╝╚═╝╚═╝╚╝─╚═╝╚╩╝
──────────  ──────────────────────────────"""

rkn1 = Config()
