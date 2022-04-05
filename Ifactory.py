#Ifactory

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import detectInformation

##import yagmail

def saveMessage(Message: str):
    return str
    #mail
##    yagmail.SMTP('oleksii.turuta@nure.ua').send('oleksii.turuta@nure.ua', 'Why,Oh why!' + "\n"+update.message.text)
    #saveToSql()

def desInformationText(update: Update):

    return str(detectInformation.desInformationText(update.message.text))


##def desInformation(update: Update):
##
##    disInformationLevel = detectInformation.desInformationText(update.message.text)
##    result = str(disInformationLevel)
##    ## + "\n" + update.message.text
##
##    return result
