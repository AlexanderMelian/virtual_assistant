import os


def get_telegram_token():
    return os.getenv('TELEGRAM_TOKEN', None)