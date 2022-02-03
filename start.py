from telegram.ext import Updater, CommandHandler


# FUNCIONES

def start(update, context):

    update.message.reply_text('Hola mundo!')

def help(update, context):

    update.message.reply_text('En que puedo ayudarte')

def contact(update, context):

    update.message.reply_text('t.me/Luis0H')



if __name__ == '__main__':

    updater = Updater(token='TOKEN', use_context='True')

    dp = updater.dispatcher

    # COMANDOS

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('contact', contact))