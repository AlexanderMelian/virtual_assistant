import os

def get_telegram_token():
    return os.getenv('TELEGRAM_TOKEN', None)

def get_my_telegram_id():
    return os.getenv('MYTELEGRAM_CHAT_ID', None)