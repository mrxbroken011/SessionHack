import os
import logging
from typing import Optional

from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from pyromod import listen

API_ID: int = Config.API_ID
API_HASH: str = Config.API_HASH
BOT_TOKEN: str = Config.BOT_TOKEN
START_PIC: Optional[str] = Config.START_PIC

LOG = Console()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("HackBot")

# === Pyrogram Client ===
app = Client(
    "Hack",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Export
__all__ = ["app", "LOG", "logger", "START_PIC"]