#! /usr/bin/python3
# -*- coding: utf-8 -*-

#from __future__ import unicode_literals
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from hazm import Normalizer

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hello World!')

def entofa(bot, update):
	
    per = ["ﺽ", "ﺹ", "ﺙ",  "ﻕ",  "ﻑ",  "ﻍ",  "ﻉ",  "ﻩ",  "ﺥ",  "ﺡ",  "ﺝ",  "چ",  "ﺵ",  "ﺱ",  "ی",
        "ﺏ",  "ﻝ",  "ﺍ",  "ﺕ",  "ﻥ",  "ﻡ",  "ک",  "گ",  "ﻅ",  "ﻁ",  "ﺯ",  "ﺭ",  "ﺫ",  "ﺩ",  "پ",  "ﻭ"]
    
    eng = ["q",  "w",  "e",  "r",  "t",  "y",  "u",  "i",  "o",  "p",  "[",  "]",  "a",  "s",  "d",
        "f",  "g",  "h",  "j",  "k",  "l",  ";",  "'",  "z",  "x",  "c",  "v",  "b",  "n",  "m",  ","]
    s = update.message.text
    for i in range(len(per)):
        s = s.replace(eng[i], per[i])
    normalizer = Normalizer()
    s = normalizer.normalize(s)
    bot.sendMessage(update.message.chat_id, text=s)

def echo(bot, update):
    s = update.message.text
    bot.sendMessage(update.message.chat_id, text=s)

def normalizefarsi(bot, update):
    normalizer = Normalizer()
    s = normalizer.normalize(update.message.text)
    bot.sendMessage(update.message.chat_id, text=s)

def decide(bot, update):
     s = update.message.text
     if (ord(s[1]) < ord('z')): #if the input is english
         entofa(bot, update)
     else:
          normalizefarsi(bot, update)

updater = Updater('BOT TOKEN HERE')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler([Filters.text],  decide))

updater.start_polling()
updater.idle()

