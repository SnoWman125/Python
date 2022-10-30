from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from credit import bot_token
import random

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def roll(update, context):
    context.bot.send_message(update.effective_chat.id, str(random.randint(1, 6)))


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет!!!')


def help(update, context):
    context.bot.send_message(update.effective_chat.id, 'Сейчас я Вам помогу! Что случилось?')


def message(update, context):
    if update.message.text == "Бот":
        context.bot.send_message(chat_id=update.effective_chat.id, text='Привет, кожаный!')
    else:
        context.bot.send_message(update.effective_chat.id, 'пошёл в пень, кожаный!')


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Я не знаю такой команды!')


def info(update, context):
    args = context.args
    print(args)
    context.bot.send_message(update.effecrive_chat.id, 'Я бот-помощник!')


roll_handler = CommandHandler('roll', roll)
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown)
info_handler = CommandHandler('info', info)

dispatcher.add_handler(roll_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(info_handler)

updater.start_polling()
updater.idle()
