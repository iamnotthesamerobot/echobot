######## simple echo-bot ############
# -*- coding: utf-8 -*-

### my tasting bot

import telebot

echobot = telebot.TeleBot(token = '574405257:AAHRY6UBHzMs5lgBlIGZbvnxYellkHL4Pks')

@echobot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    echobot.send_message(message.chat.id, message.text)
    
if __name__ == '__main__':
    echobot.polling(none_stop=True)