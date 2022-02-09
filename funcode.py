#Probably going to be the process I use from now on. 
#I am enjoying this, it is coming together 
from tkinter import N


def funNewProgram():
    print("Welcome to the New Story Mode\n"
        "To begin the journey please write your name!")
    userName=str(input("What is your name?"))
    print("So your name is",userName,"...\n"
        "Okay, might as well fill you in on what you have missed. ")
    print("Some type of backstory... blah blah blah")
    print("First question\n"
          "This is also where the options are laid out")
    firstChoice=str(input("What option will you choose?: a, b, c, d?")) 
    if firstChoice in ['option1', '1','option_1', 'first', 'first option', 'a']:
        print("So you chose this option...")
        print("It seems you have mistaken me for a dummy")
    if firstChoice in ['option2', '2','option_2', 'second', 'second option', 'b']:
        print("A wise choice, indeed")
    if firstChoice in ['option3', '3','option_3', 'third', 'third option', 'c']:
        print("Hmmm, an interesting choice... You may prove to be useful after all...")
    if firstChoice in ['option4', '4','option_4', 'fourth', 'fourth option', 'd']:
        print("I think you will want to reconsider this...")
        print("Do you wish to choose a different option?")
        redoDecision=str(input("Yes or No?"))
        if redoDecision in ['yes', 'Yes', 'y']:
            redoChoice=str(input("What option will you choose?: a, b, c, d?")) 
            if redoChoice in ['option1', '1','option_1', 'first', 'first option', 'a']:
                print("So you chose this option...")
                print("It seems you have mistaken me for a dummy")
            if redoChoice in ['option2', '2','option_2', 'second', 'second option', 'b']:
                print("A wise choice, indeed")
            if redoChoice in ['option3', '3','option_3', 'third', 'third option', 'c']:
                print("Hmmm, an interesting choice... You may prove to be useful after all...")
        else:
            print("You have sealed your fate\n"
                  "...\n"
                  "....\n"
                  ".....\n"
                  "......\n"
                  ".......\n"
                  "......\n"
                  ".....\n"
                  "....\n"
                  "...\n"
                  "..\n"
                  "So, you want to play again?")
    choiceCont=str(input("What an interesting choice...wouldn't ya say?"))
    if choiceCont in ['y', 'Yes', 'yes']:
        print("Well since you chose that... I guess I have no option but to go with ya... that way you don't get hurt, or worse\n"
              "C'mon. We'll need to stock up on some supplies and get refreshed before we deal with the troubles of the world")
    else:
        print("Oh, whatever! You are being so undecisive! You are impossible to read and impossible to even want to be around\n"
        "If you don't shape up, I dont know how we are going to deal with the rest of this adventure!\n"
        "I'm not even sure you would live to see tomorrow if it were not for me.\n"
        "Regardless, we've got to go, I don't want to stay out here much longer.")
    return funNewProgram
funNewProgram()

