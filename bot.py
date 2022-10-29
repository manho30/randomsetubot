import json

import telebot
import requests

bot = telebot.TeleBot('TOKEN', parse_mode=None)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, '发送一个随机消息， 我会返回你一个色图')
    
@bot.message_handler(content_types=['text'])
def send_text(msg):
        bot.send_chat_action(msg.chat.id, 'upload_photo')
        bot.send_photo(msg.chat.id, json.loads(requests.get('https://api.lolicon.app/setu/v2'))['data'][0]['urls']['original'], reply_to_message_id=msg.message_id)
        
bot.infinity_polling()
