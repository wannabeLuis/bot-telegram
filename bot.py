import qrcode, os
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup

INPUT_TEXT = 0

def start(update, context):

    update.message.reply_text(
        text=f'Hola {update.effective_user.first_name} aquí puedes generar un codigo QR. \n\n Solo envía el comando /qr',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Generar QR', callback_data='qr')],
            [InlineKeyboardButton(text='Sobre el autor', url='t.me/Luis0h')],
        ])
    )

def about(update, context):
    update.message.reply_text('T.me/luis0h')

def qr_command_handler(update, context):
    update.message.reply_text(f'OK {update.effective_user.first_name} envíame el texto para generarte un código QR.')

    return INPUT_TEXT

def qr_callback_handler(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text=f'OK {update.effective_user.first_name} envíame el texto para generarte un código QR.'
    )

    return INPUT_TEXT

def generate_qr(text):
    filename = text + '.jpg'
 
    img = qrcode.make(text)
    img.save(filename)

    return filename

def send_qr(filename, chat):

    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )

    chat.send_photo(
        photo=open(filename, 'rb')
    )

    os.unlink(filename)


def input_text(update, context):

    text = update.message.text

    filename = generate_qr(text)

    chat = update.message.chat

    send_qr(filename, chat)


    return ConversationHandler.END


if __name__ == '__main__':

    updater = Updater(token='TOKEN', use_context='True')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('about', about))


    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr', qr_command_handler),
            CallbackQueryHandler(pattern='qr', callback=qr_callback_handler)
        ],

        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },

        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()