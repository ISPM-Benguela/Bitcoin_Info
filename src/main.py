import time

import urllib3

import telepot
from decouple import config

# Podes abandonar estas linhas de codigo caso nao estaras
# Usando pythonanywhere free account

proxy_url = 'http://proxy.server:3128'
telepot.api._pools = {
            'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
            }
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# FIm para pythonanywhere acctount free

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

