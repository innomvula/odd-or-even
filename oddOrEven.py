newnum = True
gamecont = ["y", "n"]
while newnum == True:
    num = int(input("what number are you thinking? "))
    if num % 2 != 0:
        print("That's an odd number! Have another?")
    else:
        print("That's an even number!!")
    while newnum == True:
        newattempt = input("New number (y/n)? ")
        if newattempt in gamecont and newattempt == "n":
            newnum = False
        elif newattempt in gamecont and newattempt == "y":
            break
        else:
            print("Wrong input!")
            
    
    