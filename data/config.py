import os
import environ
from dotenv import load_dotenv
environ.Env.read_env()


BOT_TOKEN = os.environ.get("API_TOKEN")
API_key = os.environ.get('API_key')
# admins = [
#     os.getenv("ADMIN_ID"),
# ]
#
# ip = os.getenv("ip")
#
# aiogram_redis = {
#     'host': ip,
# }
#
# redis = {
#     'address': (ip, 6379),
#     'encoding': 'utf8'
# }
