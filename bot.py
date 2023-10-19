import os

import telebot

bot_token = os.environ.get("BOT_TOKEN")

if bot_token is None:
    raise Exception("Bot token is not defined")

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
