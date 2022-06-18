import telebot
import requests
import json

bot = telebot.TeleBot('5410945602:AAFg6NUHBoA2Oq4mzUNUmhvx-DC1B3_NYs8', parse_mode=None)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, '发送一个随机消息， 我会返回你一个色图')
    
@bot.message_handler(content_types=['text'])
def send_text(msg):
        bot.send_chat_action(msg.chat.id, 'upload_photo')
        r = requests.get('https://api.lolicon.app/setu/v2')
        data = json.loads(r.text)
        pic = data['data'][0]['urls']['original']
        bot.send_photo(msg.chat.id, pic, reply_to_message_id=msg.message_id)
        
bot.infinity_polling()