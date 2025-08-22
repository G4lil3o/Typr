import wonderwords
from wonderwords import RandomWord
import getpass

text = ""

def toType():
    print(text)

user_input = ""
def userInput():
    global user_input
    user_input = getpass.getpass(">>>")

def check():
    if user_input == text:
        return 0
    else:
        print("Incorrect. Try again.")
        toType()
        userInput()

def newText():
    global text
    text = RandomWord().word()

newText()
while True:
    toType()
    userInput()
    check()
    newText()
