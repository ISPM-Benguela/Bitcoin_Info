import time
import urllib3

import telepot
from decouple import config


TOKEN = config('TOKEN')

try:
    print(TOKEN)
    print("TOKEN is working...")
except:    
    print("Not working")


