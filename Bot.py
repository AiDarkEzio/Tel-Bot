# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext

# print("Bot Is starteing")

# def hello(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Hello {update.effective_user.first_name}')


# updater = Updater('1995592291:AAHciO-rtY7TrdE3e1qVRLcc4UmBxLjBzYw')

# updater.dispatcher.add_handler(CommandHandler('hello', hello))

# updater.start_polling()
# updater.idle()