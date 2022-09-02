from pydoc import render_doc
import re
import sqlite3
import getpass
from flask import Flask, render_template
import webbrowser
from threading import Timer
from sqlStatements import *

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

def connect(username):
    con = sqlite3.connect(f"/Users/{username}/Library/Messages/chat.db")
    con.create_function("REGEXP", 2, regexp)
    return con

def getResults(query):
    db = connect(getpass.getuser())
    cur = db.cursor()
    cur.execute(query)
    return cur.fetchall()







app = Flask(__name__)
@app.route("/")
def main():
    mostSent2 =getResults(mostSentText2())
    mostSent5 =getResults(mostSentText5())
    mostTalked =getResults(mostTalkedToQuery())
    timeReceived24 =getResults(textReceivedByTimeQuery())[0][0]
    if int(timeReceived24)>12:
        mornNightReceived="PM"
    else:
        mornNightReceived="AM"
    timeSent24 =getResults(textSentByTimeQuery())[0][0]
    if int(timeSent24)>12:
        mornNightSent="PM"
    else:
        mornNightSent="AM"
    timeReceived12 = (int(timeReceived24)-12)
    timeSent12 = (int(timeSent24)-12)
    sentNight = getResults(textSentNightQuery())



    
    return render_template('index.html', 
    mostSent2_1         = mostSent2[0][0],
    mostSent2_2         = mostSent2[1][0],
    mostSent2_3         = mostSent2[2][0],
    mostSent5_1         = mostSent5[0][0],
    mostSent5_2         = mostSent5[1][0],
    mostSent5_3         = mostSent5[2][0],
    mostTalked_1        =mostTalked[0][0],
    mostTalked_2        =mostTalked[1][0],
    mostTalked_3        =mostTalked[2][0],
    mostTalked_4        =mostTalked[3][0],
    mostTalked_5        =mostTalked[4][0],
    charsSent           =getResults(totalCharsSentQuery())[0][0],
    textReceived        =getResults(totalTextReceivedQuery())[0][0],
    charsReceived       =getResults(totalCharsReceivedQuery())[0][0],
    textSent            =getResults(totalTextSentQuery())[0][0],    
    #longestReceived     =getResults(longestTextReceivedQuery()),
    #longestSent         =getResults(longestTextSentQuery()),
    timeReceived        =timeReceived12,
    amPmReceived        = mornNightReceived,
    amPmSent            = mornNightSent,
    timeSent            =timeSent12,
    sentNight_1        =sentNight[0][0],
    sentNight_2        =sentNight[1][0],
    sentNight_3        =sentNight[2][0],
    sentNight_4        =sentNight[3][0],
    sentNight_5        =sentNight[4][0],
    nightTextReceived   =getResults(textReceivedNightQuery()),
    morningTextSent     =getResults(textSentMorningQuery()),
    morningTextReceived =getResults(textReceivedMorningQuery())
    )


def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')
      
if __name__ == '__main__':
    Timer(1,open_browser).start()
    app.run(port=5000)

