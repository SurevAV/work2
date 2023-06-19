#import oas
from dataclasses import dataclass



bot_token = "6039886909:AAE0OP7R_6XG2xZv2uTf3WO4bZjUG1wJgvo"


db_name = 'test'
db_user = 'postgres'
db_pwd = 'user'
db_host = 'localhost'
db_port = 5432


@dataclass
class Config:
    DB_NAME = db_name
    DB_USER = db_user
    DB_PASSWORD = db_pwd
    DB_HOST = db_host
    DB_PORT = db_port
    BOT_TOKEN = bot_token

    PAYMENTS_PROVIDER_TOKEN = '401643678:TEST:a6146ff1-02c9-40a0-aac7-f33bec7c7bbf'
