from cgitb import text
from telegram.ext import Updater, MessageHandler, Filters


def process_message(update, context):

    text = update.message.text

    if str(text).__contains__('#channel'):
        context.bot.send_message(
            chat_id='-1001334822326',
            text=str(text).replace('#channel', '')
        )


if __name__ == '__main__':

    updater = Updater(token='YOUR TOKEN', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))
    
    updater.start_polling()

    print('Bot is polling')

    updater.idle()


