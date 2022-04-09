#detectInformation
#from telegram import Update, ForceReply
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import modSQL

def desInformationText(Message: str):


    print(Message)
    # insert into SQL lite
    conn = modSQL.create_connection()
    modSQL.insert_msg(conn, Message)
    modSQL.close_connection(conn)

    # Simple extimation
    # count Top symbols
    # stop words
    # Detection:
    # Phone - Regexp
    # what Regexp provide else?
    # Language Detection
    #NLP basic
    # ML
    # NER
    # Sentiment
    # Classification
    # Visualization
    #

    return "Рівень достовірності інформації = " + str(0.5)

#def desInformation(update: Update):
#    disInformationLevel = desInformationText(update.message.text)
#    result = str(disInformationLevel)
    ## + "\n" + update.message.text
#
#    return result
def ListOfMessage():
    conn = modSQL.create_connection()
    rows = modSQL.select_msg(conn, "select id, msg from MESSAGES order  by id  DESC limit 11")
    result = ""
    for row in rows:
        result +=  str(row[0]) + ") " + str(row[1])[0:200] + "\n\n"

    modSQL.close_connection(conn)
    return result
