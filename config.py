from pyrogram import Client
from asBASE import asJSON
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

db = asJSON("as.json")
###


SUDORS = int(getenv("SUDORS", 5901732027))
API_ID = getenv("API_ID","20036317")
API_HASH = getenv("API_HASH","986cb4ba434870a62fe96da3b5f6d411")
TOKEN = getenv("TOKEN")
bot = Client("control",API_ID,API_HASH,bot_token=TOKEN,in_memory=True)
bot_id = TOKEN.split(":")[0]
