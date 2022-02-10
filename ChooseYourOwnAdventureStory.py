#Probably going to be the process I use from now on. 
#I am enjoying this. Let's make sure that this is somewhat finished and in good place for when I want to run it and possibly give it up for downloading :).


def ChooseYourOwnAdventureStory():
    print("Welcome and thanks for reading and playing! This is my first project so I know it can be crude and even might not be fun to play, but who cares!\n"
        "Let's get to the actual game now :)\n"
        "To begin the journey please write your name!")
    userName=str(input("What is your name?"))
    print("So your",userName,"...\n"
        "Okay, might as well fill you in on what missed. It seems that you have missed quite a lot, not sure how... but you did. Basically, the entire land of Algoraea has been thrusted into a civil war!\n"
        "However, this isn't just some civil war that can be culled through diplomatic means, no, this can only be calmed through the complete decimation of all those who 'oppose(d)' the old king.\n" 
        "The proud old king, Yovlosh, in a fit of rage and pure delusion, declared that any subject who has ancestral blood ties to dwarves, elves, and anything inbetween\n"
        #Yovlosh is pronounced like YO-veL-aw-Sch, old king whom has extreme race prejudice and is the entire founder of the civil war 
        "are to be expunged for their tainted blood."
    
        "Place holder line" )
    toContinue=str(input("Are you ready to continue? Yes or no?"))
    if toContinue in ['y', 'yes', 'Yes']:
        print("First question\n"
          "This is also where the options are laid out\n"
          "a)...\n"
          "b)...\n"
          "c)...\n"
          "d")
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
                    "So, you want to choose again?")
        choiceCont=str(input("What an interesting choice...wouldn't ya say?"))
        if choiceCont in ['y', 'Yes', 'yes']:
            print("Well since you chose that... I guess I have no option but to go with ya... that way you don't get hurt, or worse\n"
              "C'mon. We'll need to stock up on some supplies and get refreshed before we deal with the troubles of the world")
        else:
            print("Oh, whatever! You are being so undecisive! You are impossible to read and impossible to even want to be around\n"
            "If you don't shape up, I dont know how we are going to deal with the rest of this adventure!\n"
            "I'm not even sure you would live to see tomorrow if it were not for me.\n"
            "Regardless, we've got to go, I don't want to stay out here much longer.")
    else:
        for toContinue in range [1]:
            break
    
ChooseYourOwnAdventureStory()
