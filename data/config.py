import os
import environ
from dotenv import load_dotenv
environ.Env.read_env()


BOT_TOKEN = os.environ.get("API_TOKEN")
API_key = os.environ.get('API_key')
