from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyMarkup
from telegram.ext import Updater, CommandHandler

def start(update, context):

    button = InlineKeyboardButton(
        text='Sobre el autor',
        url='t.me/luis0h'
    )

    button1 = InlineKeyboardButton(
        text='iobyte',
        url='t.me/iobyte'
    )

    button2 = InlineKeyboardButton(
        text='Shop',
        url='t.me/PachucaHgo'
    )


    update.message.reply_text(
        text='Haz clic en un boton',
        reply_markup=InlineKeyboardMarkup([
            [button],
            [button1, button2],
        ])
    )

if __name__ == '__main__':

    updater = Updater(token='TOKEN', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()