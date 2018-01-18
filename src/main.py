import time
import urllib3

import telepot
from decouple import config


TOKEN = config('TOKEN')
bot = telepot.Bot(TOKEN)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, "You said '{}' ".format(msg['text']))

bot.message_loop(handle)

print('Listing...')
while 1:
    time.sleep(10)

