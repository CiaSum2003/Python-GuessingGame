# Cianee Sumowalt
# Homework 5 Guess the Digits
# October 11, 2022

import random
print ("\n Guess the 4- digit random nonnegative integer - no repeats")
print ("As the program proceeds, the computer will tell you")
print ("\n if a digit appears in the number, and, if it does, what its position is.")
print ("\n Good Luck")

def getRandom():
    compNo = ""
    length = 0
    tries = 0
    while len(compNo) < 4:
        compRan = chr(random.randint(48,57))
        tries = tries + 1
        if compRan not in compNo:
            compNo = compNo + compRan
            length = length + 1
    return compNo #This function determines the number randomly generated!

compNo = getRandom()
gameWin = "No"

while gameWin == "No":
    userGuess = input ("\n Enter a four digit number with no repeats: ")
    if userGuess == compNo:
        print ("You have all the right answers and they're all in the correct position! You win!")
        gameWin == "Yes" #This skips to the end, so you don't get told if everything is in the correct position. It's kind of implicit
        break
    else:
        yesDigit = 0
        yesPos = 0
        for i in userGuess:
            if i in compNo:
                yesDigit += 1
                if userGuess.index(i) == compNo.index(i):
                    yesPos += 1
                    yesDigit -= 1
                    print (f"{i} is in the correct position.")
                else:
                    print (f"{i} is correct.")
            else:
                print (f"{i} is incorrect. ")






