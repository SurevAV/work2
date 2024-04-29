#import oas
from dataclasses import dataclass



bot_token = ""


db_name = 'test'
db_user = 'postgres'
db_pwd = 'user'
db_host = 'localhost'
db_port = 5432

#main_db main_user it1234
@dataclass
class Config:
    DB_NAME = db_name
    DB_USER = db_user
    DB_PASSWORD = db_pwd
    DB_HOST = db_host
    DB_PORT = db_port
    BOT_TOKEN = bot_token

    PAYMENTS_PROVIDER_TOKEN = ''
