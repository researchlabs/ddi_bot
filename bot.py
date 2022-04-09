#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
#TODO
# how to add estimation of messages
# visualisation result
# how ask vebbose desInformation
# ?some kind of setting
# search similar messages


import logging
import Ifactory

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    # {user.mention_markdown_v2()}\
    #    msg = "Добридень\n"\
    #    msg = "Добридень{user.mention_markdown_v2()}\n"\

    msg = "Добридень\n"\
    + "Вас вітає сервіс з виявлення дезинформації"

    update.message.reply_markdown_v2(msg,
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    msg = "Допомога:\n"\
    + "1) Сервіс аналізу повідомлень.\n"\
    + "2) Сервіс перегляду повідомлень, які були надіслані."

    update.message.reply_text(msg)

def list_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /list is issued."""
    msg = Ifactory.desInformationListOfMessage(update)

    update.message.reply_text(msg)

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    str_out = Ifactory.desInformationText(update)

    update.message.reply_text(str_out)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5126036157:AAGJ_QkcsSC-mbNHOnigwtwyeEPhkUiUiwk", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("list", list_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot

    updater.start_polling()

#updater.start_webhook(listen="0.0.0.0",
#                          port=int(PORT),
#                          url_path=TOKEN)
#updater.bot.setWebhook('https://protected-sea-48938.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
