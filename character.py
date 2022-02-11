def Character():
    characterCreation=1
    print("Here we are going to create your character. Dress them up as you like, how you like, etc. Keep in mind the target is to be creative but keep it realistic within fantasy")
    characterAge=eval(input("What is the age of your character?:"))
    race=str(input("What race is your character?:"))
    eyeColorRight=str(input("Right eye color: "))
    eyeColorLeft=str(input("Left eye color: "))
    skinTone=str(input("Skin tone: "))
    hairColor=str(input("Hair Color: "))
    hairColorHighlight=str(input("Any highlights in the hair?: "))
    bodyLength=str(input("How tall is your character?: "))
    bustSize=str(input("What type of bust does your character have?: "))
    muscle=str(input("Is your character muscled? Burly? Skrawny? Toned? Or write your own!: "))
    print("List a few specific traits you would like your character to have? (Ex. Tough skin, past full of trauma, horny, studious, etc.")
    specificTraitLimit=1
    print("Please choose wisely, as your character can only be graced with 3 specific traits.")
    for i in range (specificTraitLimit):
        characterTraitsA=str(input())
        characterTraitsB=str(input())
        characterTraitsC=str(input())
    print("Hm, it appears you have:",characterTraitsA,",",characterTraitsB,", and",characterTraitsC,",","for your traits... I don't know of anyone with those specific traits. I guess there is a first time for everything.")
    characterCreationContinuation= str(input("Are you ready to continue?"))
    if characterCreationContinuation in ['y', "yes", "Yes"]:
        print("Great! Enjoy the adventure!")
    else:
        for i in range (characterCreation):
            Character()