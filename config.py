from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")
    
    OWNER_ID = int(getenv("OWNER_ID", "7044783841"))

    START_PIC = getenv("START_PIC", "https://files.catbox.moe/cd2zru.jpg")