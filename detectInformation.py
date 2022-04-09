#detectInformation
#from telegram import Update, ForceReply
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import modSQL
import re
#https://www.w3schools.com/python/python_regex.asp

def desInformationText(Message: str):


    print(Message[0:200])
    Istina = {}
    Istina['k1'] = getK1_alarmTitle(Message)
    Istina['k10'] = getK10_inside(Message)
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
    str_out = istinaDecode(Istina) + "\n" + istinaResult(Istina)

    return str_out

def istinaDecode(istina):
    str_out = str(istina)
    return str_out

def istinaResult(istina):
    kPositive = 0
    kTotal = len(istina)
    for item in istina:
        kPositive += int(istina[item])
    str_out = "Рівень достовірності інформації = " + str(kPositive) + " / " + str(kTotal)
    return str_out

def getK1_alarmTitle(Message:str):
    K1=0
    x = -1
    x = re.search("!!!!+", Message)

    if x:
        K1 = 1
    return K1

def getK10_inside(Message:str):
    K1=0
    x = -1
    x = re.search("я точно знаю", Message)

    if x:
        K1 = 1
    return K1

def ListOfMessage():
    conn = modSQL.create_connection()
    rows = modSQL.select_msg(conn, "select id, msg from MESSAGES order  by id  DESC limit 11")
    result = ""
    for row in rows:
        result +=  str(row[0]) + ") " + str(row[1])[0:200] + "\n\n"

    modSQL.close_connection(conn)
    return result
