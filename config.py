## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBAjOR32fITzOwoCyTy4qM-rmCtcUf4RB8BPm_yKTfhU1I657yhG2c1bdeD8Lfat5TRr-nGcbTjFU0tu4VYUonrY1tlaHAN_Gv85tU_YKNlUQQ91v5iQeUyOCCSu8QmJR9XtLUk_e6tufRKvfNnWIjb5ByzLgslxRDhQ6HOMxcCnlRzGz9_FyHnrxIKZmj3gbGssJLVzoxIw6W04ON36wBgLl1aGNBl0-JJEjTcQ8pMRa6WBZC1Uh5yFqLSYcegpzGMpP29ek6cIjuDNBejEcPpI1-u7sR4_rnFhXYxBdluKwJOvdtwFwkKSkj0e1wlQA9zOA4DVcScdXFo7T8PTApPcNBJPgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5365204439:AAEg9NRnfdvOgxDoGSNztuWhC3i3Gqzo1Q0")
BOT_NAME = getenv("BOT_NAME", "𝗠𝗨𝗦𝗜𝗖 𝙂𝙄𝘼𝙉𝙏𝙎 𝅘𝅥𝅮")
API_ID = int(getenv("API_ID", "16847236"))
API_HASH = getenv("API_HASH", "0850c6613c18ce6eb65dce400355faa5")
OWNER_NAME = getenv("OWNER_NAME", "حنتوش ꪋᥣ T𝗈ƙꪗ᥆")
OWNER_USERNAME = getenv("OWNER_USERNAME", "btb3e")
ALIVE_NAME = getenv("ALIVE_NAME", "حنتوش")
BOT_USERNAME = getenv("BOT_USERNAME", "mc_6bot")
OWNER_ID = getenv("OWNER_ID", "1466286671")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "btb3a")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "A3HHHH")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "x8_u6")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1466286671").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/46fa55b49b85c084159ce.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/466de30ee0f9383c8e09e.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
