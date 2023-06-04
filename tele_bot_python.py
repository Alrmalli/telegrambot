import telegram
import time

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

bot = telegram.Bot(token=TOKEN)

while True:
    bot.send_message(chat_id=CHAT_ID, text='Your message here test 5 min intervals')
    time.sleep(300) # sleep for 300 seconds (5 minutes)