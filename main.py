import random

userChoice = str(input("Choose between R, P, S,"))

selectedChoice = (random.choice(["Rock","Paper","Scissors"]))

if userChoice == "R" and selectedChoice == "Rock":
    print("It was a tie!")
elif userChoice == "R" and selectedChoice == "Paper":
    print("The computer won!")
elif userChoice == "R" and selectedChoice == "Scissors":
    print("You won!")
elif userChoice == "P" and selectedChoice == "Scissors":
    print("The computer won!")
elif userChoice == "P" and selectedChoice == "Paper":
    print("It was a tie!")
elif userChoice == "S" and selectedChoice == "Scissors":
    print("It was a tie!")
