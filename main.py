from telegram import Update
from telegram.ext import *
import Data_Base.Config as Key
import Modules.Respon as Res

def start_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help_command(update, context):
    update.message.reply_text("dfdj324685hrvkkshfefkrekhfs3458734reyfuw")
    
def handle_message(update, context):
    text = str(update.message.text).lower
    response = Res.sample_responses(text)
    
    update.message.reply_text(response)
    
def error(update, context):
    print(f"Update {update} causted error {context.error}")
    
def main():
    updater = Updater(Key.API_KEY, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(error)
    
    updater.start_polling()
    updater.idle()

main()

###################################################################################################

# def main(password):
#     if(password == "poshitha"):
#         updater = Updater(Key.API_KEY, use_context=True)
#         dp = updater.dispatcher
        
#         dp.add_handler(CommandHandler("start", start_command))
#         dp.add_handler(CommandHandler("start", help_command))
#         dp.add_handler(MessageHandler(Filters.text, handle_message))
#         dp.add_handler(error)
        
#         updater.start_polling()
#         updater.idle()

#     else:
#         return print("Your Password Is Incorret")

###################################################################################################