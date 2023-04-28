import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

env_path = "settings.env"
load_dotenv(env_path)

token = os.environ.get("BOT_TOKEN")