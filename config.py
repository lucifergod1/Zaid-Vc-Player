## What's up Kangerss

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAx8ftZtQAuTXYeVTpfia6uOmrXqYtawpe2XXBavEx202THoDle5rHCfduXQC5hY4y87LN0F39uzhtfVmu6Y5jooVh1ur-PDQgRYZEH156nELxZhQY2MwMK6lep0FT1RPn3D-EVvzUb1v-poHUALNgtrnDUcrR8cjo-ana8VhNOx5YselWM-IXm0BqCQJgkPWjalREVljBc-ANccB0MLxUCP0rHBKJpo3LkVHni0UJ1jumTKkm3q94ZI48mCkcpTZQipQtDOErGCcPaJgyLHG5pSNRJhx1521Jv-p7ORRY1cVfGNwq5cnclw5LREiI1cH28BouFigjlgm2Tr6H43Q0vV1dOpAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5318089386:AAEhtSj-BrTzEnZ4sLWUyP9h0U5biWY9aq8")
BOT_NAME = getenv("BOT_NAME", "Sakura")
API_ID = int(getenv("API_ID", "5245830"))
API_HASH = getenv("API_HASH", "e9d7b164840e974b702cb11f10ce85d7")
OWNER_NAME = getenv("OWNER_NAME", "Lucifer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Hey_Its_Me_Lucifer")
ALIVE_NAME = getenv("ALIVE_NAME", "Sakura")
BOT_USERNAME = getenv("BOT_USERNAME", "Sakura_Vc_Bot")
OWNER_ID = getenv("OWNER_ID", "1382567771")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "@Sakura_Xd_69")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "movie_sector")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "The_Devloper_Network")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1272039806 1382567771").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/0e08ecd6046987d5e117e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/lucifergod1/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
