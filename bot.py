import os

import telebot
from telebot import types

from AsosCrawler import AsosCrawler

bot_token = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Start message")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Instructions")


@bot.message_handler(func=lambda msg: True)
def return_size_from_asos_item(message):
    asos_crawler = AsosCrawler(url=message.text, binary_location="", driver_location="")
    sizes = asos_crawler.get_sizes()
    markup = types.InlineKeyboardMarkup(row_width=2)
    for size in sizes:
        markup.add(types.InlineKeyboardButton(text=size, callback_data=size))
    bot.send_message(message.chat.id, "Choose desired size", reply_markup=markup)


@bot.callback_query_handlers(func=lambda call:True)
def notify_on_size(callback):
    pass

bot.infinity_polling()
