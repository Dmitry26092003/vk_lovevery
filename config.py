from dataclasses import dataclass
from dotenv import load_dotenv
from os import getenv

load_dotenv()


@dataclass
class Settings:
    user_token = getenv('USER_TOKEN')
    bot_token = getenv('BOT_TOKEN')
    group_id = 217496604
