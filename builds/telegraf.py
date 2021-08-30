import tokens

# ###############
from telegram.ext import Updater, MessageHandler, Filters

def messageFilter(update, context):#This can filter messages
    print("Hi")

def send_message(my_text):
    dp.bot.send_message(chat_id=my_telegram_id, text=my_text)

my_telegram_id = tokens.get_my_telegram_id()
telegram_token = tokens.get_telegram_token()
if telegram_token == None:
    print("Invalid token")

updater = Updater(token=telegram_token, use_context=True)

dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text, messageFilter))

updater.start_polling()
