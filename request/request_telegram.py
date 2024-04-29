import requests
from data.config import Config
async def send_to_user(chat, text):
    token = Config.BOT_TOKEN
    chat_id = chat
    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    return requests.get(url_req)