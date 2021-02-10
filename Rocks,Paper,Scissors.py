from random import randint

list = ["Rock", "Paper", "Scissors"]

computer = list[randint(0,2)]
score1 = 0
score2 = 0

player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            print(score1,"-",score2)
            score2 = score2+1
        else:
            print("You win!", player, "smashes", computer)
            print(score1,"-",score2)
            score1 = score1+1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            print(score1,"-",score2)
            score2 = score2+1
        else:
            print("You win!", player, "covers", computer)
            print(score1,"-",score2)
            score1 = score1+1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            print(score1,"-",score2)
            score2 = score2+1
        else:
            print("You win!", player, "cut", computer)
            print(score1,"-",score2)
            score1 = score1+1
    else:
        print("That's not a valid play. Check your spelling!")
    computer = list[randint(0,2)]