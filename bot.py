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


@bot.message_handler(func=lambda message: message.new_chat_members is not None)
def welcome_new_members(message):
    for user in message.new_chat_members:
        bot.send_message(message.chat.id, f"Welcome to Asos Notifier Bot, {user.first_name}!\n"
                                          f"Please send a link to the item you would like to be notified.\n"
                                          f"After sending, choose a size.")


bot.infinity_polling()
