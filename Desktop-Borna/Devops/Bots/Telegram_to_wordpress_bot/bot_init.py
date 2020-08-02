# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from telegram import Update
from telegram.ext import (MessageHandler, Filters, Updater, CommandHandler,
                          CallbackQueryHandler, CallbackContext)
import 

# ─── CONSTANTS ──────────────────────────────────────────────────────────────────
TG_TOKEN = #insert bot token here


def start_bot():
    updater = Updater(TG_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    init_handler = CommandHandler('start', start, pass_args = True)
    send_jsons = CommandHandler('send_json', send_jsons)
    
    dispatcher.add_handler(init_handler)
    dispatcher.add_handler(send_jsons)

    updater.start_polling()


def start(update, context):
    chat_id = update.effective_message.id
    context.bot.send_message(chat_id = chat_id, text = 'Hello and welcome to our telegram bot!')


if __name__ == "__main__":
    start_bot()