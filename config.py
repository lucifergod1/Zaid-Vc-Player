## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQB--jncuLjQd9Y0wMYlvDod1O-uVxO9T4A5MQzntAmtTb8oYVpxL03RBcpbj1OYnatv2IuFHMlUr7jPE2S9ZWpdn35ugw7XJBKYGT3GelFrtFnqWgfowqElsHbG_6eoKB6vCzuflA5Rznbgd-cXqTIJOqmhAgTQNqS8kuTzAAfvqyQ8QsEaWoOLbifIisO73ODT3Qy6gOjaUkqiUytB_hiPxKrQCBzFIVz5sPjbuizWnjnd4HTrCjwLbJP-TQgRy9KhGp2cNCZbcvnFbc2ofvNrs8vlIRJL3UXfsFWCvyFPbNwz_BGIQglLJeclQv92qO0aWOUB4vOpzZRmjzcOHkeTZxdjFQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5318089386:AAE7QBMGeFLuiq3LFsWJAjOuvez272JhmgA")
BOT_NAME = getenv("BOT_NAME", "Sakura")
API_ID = int(getenv("API_ID", "7443070"))
API_HASH = getenv("API_HASH", "8c450401331e65dee034defc229ec0eb")
OWNER_NAME = getenv("OWNER_NAME", "Howl")
OWNER_USERNAME = getenv("OWNER_USERNAME", "iAmLiKu1")
ALIVE_NAME = getenv("ALIVE_NAME", "Sakura")
BOT_USERNAME = getenv("BOT_USERNAME", "Sakura_Vc_Bot")
OWNER_ID = getenv("OWNER_ID", "1272039806")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Sakura_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "movie_sector")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "The_Devloper_Network")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1272039806 1382567771 1729585941").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/lucifergod1/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
