from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("your_own_API_Token got from BotFathe",use_context=True)
#for when user enter /start
def start(update: Update, context: CallbackContext):
	update.message.reply_text("Hello, Welcome to the Bot .Please write \help to see the commands available.")
#for when user enter /help
def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-/youtube - To get the youtube URL/linkedin - To get the LinkedIn profile URL/google - To get the googlr URL""")

#for when user enter /youtube
def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube Link =>\https://www.youtube.com/")

#for when user enter /linkdin
def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text("Linkedin URL => \https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")
#for when user enter /google
def google_url(update: Update, context: CallbackContext):
	update.message.reply_text("Google URL => https://www.google.com/")

#for when user enter unknown command
def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

#for when user enter unknown text
def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('google', google_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) 
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
