from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext import *
import responses as R
import api

print("Bot Started....")


def start_commend(update, context):
    update.message.reply_text('Hi!')


def help_commend(update, context):
    update.message.reply_text('This is a Help')


def instagram_url(update: Update, context: CallbackContext):
    update.message.reply_text('Link')


def handel_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f'Update {update} caused error {context.error}')


def main():
    updater = Updater(api.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_commend))
    dp.add_handler(CommandHandler("help", help_commend))
    dp.add_handler(CommandHandler("instagram", instagram_url))



    dp.add_handler(MessageHandler(Filters.text, handel_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
