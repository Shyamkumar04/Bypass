from os import getenv
from time import time
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.enums import ParseMode
from logging import getLogger, FileHandler, StreamHandler, INFO, ERROR, basicConfig
from uvloop import install

install()
basicConfig(format="[%(asctime)s] [%(levelname)s] - %(message)s", #  [%(filename)s:%(lineno)d]
            datefmt="%d-%b-%y %I:%M:%S %p",
            handlers=[FileHandler('log.txt'), StreamHandler()],
            level=INFO)

getLogger("pyrogram").setLevel(ERROR)
LOGGER = getLogger(__name__)

load_dotenv('config.env', override=True)
BOT_START = time()

class Config:
    BOT_TOKEN = getenv('BOT_TOKEN', '6483614941:AAHh29t094DFXdaoIFUld9jEKI4yWytCAzU')
    API_HASH  = getenv('API_HASH', 'aecbe5f3d18bc8eed18121063e6c1a24')
    API_ID    = getenv('API_ID', '14142245')
    if BOT_TOKEN == '' or API_HASH == '' or API_ID == '':
        LOGGER.critical('ENV Missing. Exiting Now...')
        exit(1)
    AUTH_CHATS      = getenv('AUTH_CHATS', '').split()
    OWNER_ID        = int(getenv('OWNER_ID', 6483614941))
    DIRECT_INDEX    = getenv('DIRECT_INDEX', 'https://tomenbypass.kingfondness.workers.dev').rstrip('/')
    LARAVEL_SESSION = getenv('LARAVEL_SESSION', '')
    XSRF_TOKEN      = getenv('XSRF_TOKEN', '')
    GDTOT_CRYPT     = getenv('GDTOT_CRYPT', 'aFRvYU1nK2xkZFJ2UDN2R3JrN3ZDMWxNWWZUcGQzSEV5cUE5WDRLOGNOND0%3D')
    DRIVEFIRE_CRYPT = getenv('DRIVEFIRE_CRYPT', '')
    HUBDRIVE_CRYPT  = getenv('HUBDRIVE_CRYPT', '')
    KATDRIVE_CRYPT  = getenv('KATDRIVE_CRYPT', '')
    UPTOBOX_TOKEN   = getenv('UPTOBOX_TOKEN', '0ec36689a04dc6b84dbb1637b5e3f572c9ffo')
    TERA_COOKIE     = getenv('TERA_COOKIE', 'Yb_U18HteHuiyMoqmHWS7oVsUQZL2JIH_qaGTLwT')

Bypass = Client("FZ", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN, plugins=dict(root="FZBypass/plugins"), parse_mode=ParseMode.HTML)
