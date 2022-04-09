#Ifactory

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import detectInformation
import modSQL

##import yagmail

def saveMessage(Message: str):
    conn = modSQL.create_connection()
    modSQL.insert_msg(conn, Message)
    modSQL.close_connection(conn)
    return str

def desInformationText(update: Update):
    saveMessage(update.message.text)
    return str(detectInformation.desInformationText(update.message.text))

def desInformationListOfMessage(update: Update):
    return str(detectInformation.ListOfMessage())
